import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY


def send_email(email):
    message = Mail(
        from_email='admin@helikopter.com',
        to_emails=email,
        subject='Someone has tried to access a prohibited website',
        html_content='Someone has tried to access a website that you have blocked. Previous links can be checked in your account.')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
