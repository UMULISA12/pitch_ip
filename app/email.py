from flask_mail import Message
from flask import render_template
from . import mail


def mail_message(subject,template,to,**kwargs):
    sender_email="umulisaa0@gmail.com"
    sender_password="its_a_secret"
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)