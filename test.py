import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msg = MIMEMultipart('alternative')

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("otoelbakidze2020@gmail.com", "iyazfbrcmtoiebqo")
html = "You Have Successfully Ordered!"
part1 = MIMEText(html, 'html')
msg.attach(part1)
server.sendmail("otoelbakidze2020@gmail.com", "otarelbakidze105@gmail.com", msg.as_string())
server.quit()