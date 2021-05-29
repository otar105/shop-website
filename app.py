from flask import Flask, render_template, request, redirect, session
from flask.helpers import flash
from main import get_food, get_info, get_email, add_food, edit, delete_food, add_order, get_orders, get_order, delete_order_id, edit_admin, orderby, orderbypopular, orderbypricehigher, orderbypricelow, get_phones, get_headphones, get_computers, get_search, add_message, get_messages, remove_message, find_message, delete_order_code
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msg = MIMEMultipart('alternative')

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("otoelbakidze2020@gmail.com", "iyazfbrcmtoiebqo")

app = Flask(__name__)
app.secret_key = "web"

@app.route("/")
def index_page():
    if "admin" in session:
        return redirect("/admin")
    return render_template("index.html", phones = get_phones(), headphones=get_headphones(), computers = get_computers())

@app.route("/product/<id>")
def info_page(id):
    food = get_info(id)
    return render_template("details.html", food=food)

@app.route("/login")
def login_page():
    if "admin" in session:
        return redirect("/admin")
    return render_template("login.html")

@app.route("/logout")
def logout_page():
    session.pop("admin",None)
    flash("Successfully Loged Out")
    return redirect("/")

@app.route("/loginsave", methods=["post"])
def loginsave_page():
    name = request.form["email"]
    password = request.form["password"]
    emails = get_email()
    for info in emails:
        if name == info[1] and password == info[2]:
            session["admin"] = info[0]
            flash("Successfully Loged In")
            return redirect("/admin")
    flash("email or password is incorect")
    return render_template("login.html")

@app.route("/admin")
def admin_page():
    if "admin" in session:
        return render_template("admin.html", food = get_food(), count = len(get_messages()))
    return redirect("/")

@app.route("/product/create")
def create_page():
    if "admin" in session:
        flash("Succssesfully Created")
        return render_template("create.html")
    return redirect("/")

@app.route("/createsave", methods=["get"])
def createsave_page():
    name = request.args.get("name")
    image = request.args.get("image")
    description = request.args.get("description")
    price = request.args.get("price")
    group = request.args.get("group")
    stock = request.args.get("stock")
    add_food(name,image,description, price, group, stock)
    return redirect("/admin")

@app.route("/product/edit/<id>")
def edit_page(id):
    if "admin" in session:
        global editid
        editid = id
        info = get_info(id)
        flash("Succssesfully Edited!")
        return render_template("edit.html", food = info)
    return render_template("/")

@app.route("/editsave", methods=["get"])
def edit_save_page():
    name = request.args.get("name")
    image = request.args.get("image")
    description = request.args.get("description")
    price = request.args.get("price")
    groups = request.args.get("groups")
    stock = request.args.get("stock")
    print(ededid)
    edit(editid,name,image,description,price, groups, stock)
    return redirect("/admin")

@app.route("/product/delete/<id>")
def delete_page(id):
    if "admin" in session:
        delete_food(id)
        return redirect("/admin")
    return redirect("/")
    
@app.route("/orders")
def orders_page():
    if "admin" in session:
        info = get_orders()
        return render_template("orders.html", orders = info)
    return redirect("/")

@app.route("/product/order/<id>")
def order_page(id):
    food = get_info(id)
    if food[7] == 0:
        return redirect("/")
    global orderid
    orderid = id
    global ordered
    ordered = get_info(id)
    return render_template("order.html")

@app.route("/ordersave", methods=["post"])
def order_save_page():
    name = request.form["name"]
    surname = request.form["surname"]
    email = request.form["email"]
    address = request.form["address"]
    payment = request.form["payment"]
    x = "ABCDEFJHIJKLMNOPQRSTUVWXYZ"
    order_code = ""
    for i in range(0,10):
        order_code += random.choice(x)
    print(order_code)
    add_order(name,ordered[1],surname, email, address,payment, order_code, ordered[0])
    html = f"{name} You Have Successfully Ordered {ordered[1]}! Order code: {order_code}"
    msg['Subject'] = "No Reply"
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    server.sendmail("otoelbakidze2020@gmail.com", f"{email}", msg.as_string())
    flash(f"Succssesfully Ordered! Order code: {order_code}")
    return render_template("index.html", phones = get_phones(), headphones=get_headphones(), computers = get_computers())

@app.route("/orders/<id>")
def order_info(id):
    order = get_order(id)
    return render_template("order-details.html", order=order)

@app.route("/orders/remove/<id>")
def delete_order(id):
    delete_order_id(id)
    return redirect("/orders")

@app.route("/author")
def author_page():
    return render_template("author.html")

@app.route("/about")
def about_page():
    is_admin = False
    if "admin" in session:
        is_admin = True
    return render_template("about.html", is_admin = is_admin)

@app.route("/user")
def user_page():
    if "admin" in session:
        return render_template("user.html")
    return redirect("/")

@app.route("/usersave", methods=["post"])
def usersave_page():
    id = session["admin"]
    email = request.form["email"]
    password = request.form["password"]
    edit_admin(id, email, password)
    flash("Account Details Changed")
    return redirect("/")

@app.route("/orderby")
def orderby_page():
    order = orderby()
    return render_template("orderby.html", order = order)

@app.route("/orderbypopular")
def orderby_popular():
    order = orderbypopular()
    return render_template("orderbypopular.html", order = order)

@app.route("/orderbypricehigher")
def orderbypricehigher_page():
    order = orderbypricehigher()
    return render_template("orderbypricehigher.html", order = order)

@app.route("/orderbypricelow")
def orderbypricelow_page():
    order = orderbypricelow()
    return render_template("orderbypricelow.html", order = order)

@app.route("/phones")
def phones_page():
    return render_template("phones.html", phones = get_phones())

@app.route("/headphones")
def headphones_page():
    return render_template("headphones.html", headphones = get_headphones())

@app.route("/computers")
def computers_page():
    return render_template("cumputers.html", computers = get_computers())

@app.route("/search", methods=["get"])
def search_page():
    search = request.args.get("search")
    searched = get_search(search)
    if len(searched) > 0:
        flash(f"Showing result for: {search}")
        search_result = True
    else:
        flash(f"No result found for: {search}")
        search_result = False
    return render_template("search.html", searched = searched, search_result = search_result)

@app.errorhandler(404)
def invalid_route(e):
    return render_template("404page.html")

@app.route("/contact", methods=["post"])
def contact_page():
    name = request.form.get("names")
    email = request.form["email"]
    text = request.form["text"]
    add_message(name,email,text)
    flash("Sent to support team!")
    return redirect("/")

@app.route("/messages")
def messages_page():
    if "admin" in session:
        no_message = False
        if len(get_messages()) == 0:
            no_message = True
        return render_template("messages.html", messages = get_messages(), no_message = no_message)

@app.route("/reply/<id>")
def reply_page(id):
    if "admin" in session:
        global reply_id
        reply_id = id
        message = find_message(id)
        return render_template("reply.html", message = message)
    return redirect("/")

@app.route("/send", methods=["post"])
def send_page():
    email = find_message(reply_id)[0][2]
    text =  request.form["text"]
    html = f"{text}"
    msg['subject'] = "No Reply"
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    server.sendmail("otoelbakidze2020@gmail.com", f"{email}", msg.as_string())
    remove_message(find_message(reply_id)[0][0])
    flash("Message sent!")
    return redirect("/admin")

@app.route("/codesearch")
def codesearch_page():
    return render_template("code-checker.html")

@app.route("/codecheck", methods=["get"])
def codecheck_page():
    code = request.args.get("code")
    orders = get_orders()
    for i in orders:
        if i[7] == code:
            order = i
            check = True
    return render_template("code-checker.html", order = order, check = check)

@app.route("/messgae/delete/<id>")
def messagedelete_pege(id):
    if "admin" in session:
        remove_message(id)
        flash("Successfully Ignored!")
        return redirect("/messages")
    return redirect("/")

@app.route("/product/delete/code/<code>")
def deleteproduct_page(code):
    if "admin" in session:
        delete_order_code(code)
        flash("Order claimed!")
        return redirect("/codesearch")
    return redirect("/")

@app.route("/searchadmin", methods=["get"])
def searchadmin_page():
    if "admin" in session:
        search = request.args.get("search")
        searched = get_search(search)
        if len(searched) > 0:
            flash(f"Showing result for: {search}")
            search_result = True
        else:
            flash(f"No result found for: {search}")
            search_result = False
        return render_template("searchadmin.html", searched = searched, search_result = search_result)
    return redirect("/")

if __name__ == "__main__":
    app.run()