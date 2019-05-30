import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY


def send_email(email):
    message = Mail(
        from_email='admin@helikopter.com',
        to_emails=email,
        subject='Someone has tried to access a prohibited website',
        html_content='<h3>Hello,</h3><hr><br/><br/><p>Someone has tried to access a website that you have blocked. <br/><br/>A list of prohibited links may be viewed on the Link History page on <a href="https://helikopter.herokuapp.com/users/new">Your Account</a>.<br/><br/> - Sincerely, the Helikopter Team')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
