# send emails 

import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email):
    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = to_email
    msg['To'] = to_email

    # Send the email using SMTP
    with smtplib.SMTP('localhost', 1025) as server:
        server.send_message(msg)
    
if __name__ == "__main__":
    # Example usage
    subject = "Test Email"
    body = "This is a test email."
    to_email = "test@localhost.test"
    send_email(subject, body, to_email)