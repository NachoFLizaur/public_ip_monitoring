import smtplib
import ssl
from socket import gaierror
import sys

# The paramenter ip has to be passed with double quotes (i.e. "1.1.1.1")
ip = sys.argv[1]

# Specify the sender's and receiver's email addresses:
# The sender needs to have allowed the use of less secure apps in the google account config
# https://myaccount.google.com/lesssecureapps
sender = "your-email@gmail.com"
password = "your-password"
receiver = "dest-email@whatever.com"

# email message
message = f"""\
Subject: ip test 1
To: {receiver}
From: {sender}
This is the ip {ip}."""

smtp_server = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

try:
    # Send your message with credentials specified above
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
except (gaierror, ConnectionRefusedError):
    # tell the script to report if your message was sent or which errors need to be fixed
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))
else:
    print('Sent')
