import smtplib
import ssl
from socket import gaierror
import sys

ip = sys.argv[1]

# Specify the sender's and receiver's email addresses:
# The sender needs to have allowed the use of less secure apps in the google account config
# https://myaccount.google.com/lesssecureapps
sender = ""
password = ""
receiver = ""

# email message
message = 'Subject: {}\n\n{}'.format("PUBLIC_IP", """###############################
Your public ip changed to: """ + ip + """
###############################""")

# message = """\
# Subject: The IP has changed
# To: """+ receiver + """
# From: """+ sender + """
# This is the new ip: """ + ip

smtp_server = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

try:
    # Send your message with credentials specified above
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    server.quit()
except (gaierror):
    # tell the script to report if your message was sent or which errors need to be fixed
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))
else:
    print('Sent')
