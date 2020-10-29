import smtplib, ssl

# For SSL
port = 465  

# Google SMTP Server
smtp_server = "smtp.gmail.com"

# Sender address
sender_email = "your-email@gmail.com" 

# Receiver address
receiver_email = "to-email@gmail.com"

# Take password as user input
password = input("Type your password and press enter: ")

# Message to be sent
message = """\
Subject: Hacktoberfest
This message is sent from Python app contirbuted by developers."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as svr:
    svr.login(sender_email, password)
    svr.sendmail(sender_email, receiver_email, message)
