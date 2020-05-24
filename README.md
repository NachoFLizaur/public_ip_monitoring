# public_ip_monitoring
The aim of this small project is to create a program which will send the user an email whenever their public IP address is changed by their ISP

Files:

- mail_p3.py: Small python 3 program to send an email, according to the specified parameters, with the ip passed as a parameter on the email body.
- mail_p2.py: The same program but in python 2.

## How does it work?

Depending on the python installation you have, you may use one mail program or another.

In the case of the python 2 program, the mail message is quite simpler, as I had some troubles with it.

The programs take an ip address as a parameter, and then use the configuration hardcoded in the code to send an email.