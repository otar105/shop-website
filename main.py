import sqlite3

def get_food():
    sql = "select * from food;"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    food = cur.fetchall()
    con.close()
    return food

def get_info(id):
    sql = f"select * from food where id = {id};"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    food = cur.fetchone()
    view = food[5]
    view += 1
    sql1 = f"update food set views  = {view} where id = {id};"
    cur.execute(sql1)
    con.commit()
    con.close()
    return food

def get_info_id(id):
    sql = f"select * from food where id = {id};"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    food = cur.fetchone()
    con.close()
    return food

def get_email():
    sql = "select * from admin;"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    email = cur.fetchall()
    con.close()
    return email

def add_food(name, image, description, price, group, stock):
    sql = f"insert into food(name,image,description,price, views, groups, stock) values('{name}', '{image}', '{description}', {price}, 0, '{group}', '{stock}');"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def edit(id, name, image, description, price, groups, stock):
    sql = f"update food set name='{name}', image='{image}', description='{description}', price={price}, groups='{groups}', stock='{stock}' where id={id}"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def delete_food(id):
    sql = f"delete from food where id = {id}"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def add_order(name, product, surname, email, address, payment, code, foodid):
    sql = f"insert into orders(name, product, surname, email, address, payment, code, foodid) values('{name}', '{product}', '{surname}', '{email}', '{address}', '{payment}', '{code}', '{foodid}');"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    a = get_info_id(foodid)
    print(a)
    stock = a[7] - 1
    sql2 = f"update food set stock = {stock} where id = {foodid};"
    cur.execute(sql2)
    con.commit()
    con.close()

def get_orders():
    sql = "select * from orders;"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    orders = cur.fetchall()
    con.close()
    return orders

def get_order(id):
    sql = f"select * from orders where id = {id};"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    food = cur.fetchall()
    con.close()
    return food

def delete_order_id(id):
    sql = f"delete from orders where id = {id}"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def edit_admin(id, email, password):
    sql = f"update admin set email='{email}', password='{password}' where id={id}"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def orderby():
    sql = f"select * from food order by name asc;"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    orderdby = cur.fetchall()
    con.close()
    return orderdby

def orderbypopular():
    sql = f"select * from food order by views desc;"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    orderdbypopular = cur.fetchall()
    con.close()
    return orderdbypopular

def orderbypricehigher():
    sql = f"select * from food order by price desc;"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    orderdbypricehigher = cur.fetchall()
    con.close()
    return orderdbypricehigher

def orderbypricelow():
    sql = f"select * from food order by price asc;"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    orderdbypricelow = cur.fetchall()
    con.close()
    return orderdbypricelow

def get_phones():
    sql = f"select * from food where groups = 'phone';"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    phones = cur.fetchall()
    con.close()
    return phones

def get_headphones():
    sql = f"select * from food where groups = 'headphone';"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    headphones = cur.fetchall()
    con.close()
    return headphones

def get_computers():
    sql = f"select * from food where groups = 'computer';"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    computers = cur.fetchall()
    con.close()
    return computers

def get_search(s):
    sql = f"select * from food where name like '{s}%';"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    searched = cur.fetchall()
    con.close()
    return searched

def get_messages():
    sql = "select * from messages;"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    messages = cur.fetchall()
    con.close()
    return messages

def add_message(name, email, message):
    sql = f"insert into messages(name,email,text) values('{name}','{email}','{message}');"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def find_message(id):
    sql = f"select * from messages where id = {id};"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    messages = cur.fetchall()
    con.close()
    return messages

def remove_message(id):
    sql = f"delete from messages where id = {id};"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def delete_order_code(code):
    sql = f"delete from orders where code = '{code}';"
    con = sqlite3.connect("date.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()