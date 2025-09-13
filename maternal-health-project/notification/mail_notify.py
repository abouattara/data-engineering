#================================ Email notification ================================
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 5. Envoi d'email
def send_email(subject, body):
    sender_email = "data.engineer.mail@gmail.com"
    receiver_email = "stackholder.mail@gmail.com"
    password = "... ... ... ..."  # create app access to your email and get your password 

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email envoyé avec succès.")
    except Exception as e:
        print("Erreur lors de l'envoi de l'e-mail:", e)
