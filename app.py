from flask import Flask, render_template, url_for, request, flash
from flask_recaptcha import ReCaptcha
import os
import smtplib
from smtplib import SMTP_SSL as SMTP
import time


aws_key = os.environ.get('AWS_ACCESS_KEY_ID')
aws_pw  = os.environ.get('AWS_SECRET_ACCESS_KEY')

app = Flask(__name__)

secret_key = os.urandom(12)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def email_values():
    
    myemail = os.environ.get('EMAIL_USER')
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    msg = request.form['message']
    
    message = f"""From: {email}
                To: {myemail}\n
                Subject: {subject}\n
                Message: (from webpage form): {msg}"""

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(myemail, os.environ.get('EMAIL_PW'))
    server.sendmail(myemail, myemail, message)
       
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

