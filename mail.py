import smtplib
from email.message import EmailMessage

def email_alert(subject,Body,to):
    #message
    msg=EmailMessage()
    msg.set_content(Body)
    msg['subject']=subject
    msg['to']=to   
    #user 
    user="example@gmail.com"
    msg['from']=user
    password="passwordbygmail"
    #server
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_alert("hello","this is a auto generated mail","sendmail@gmail.com")