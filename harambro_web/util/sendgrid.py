import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENGRID_API_KEY


def send_email(email):
    message = Mail(
        from_email='sandraoverlord@harambro.com',
        to_emails=email,
        subject='Someone has tried to access a prohibited website',
        html_content=f'Dear {name}, someone has tried to access a prohibited website.')
    try:
        sg = SendGridAPIClient(SENGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
