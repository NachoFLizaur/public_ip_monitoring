# public_ip_monitoring
The aim of this small project is to create a program which will send the user an email whenever their public ip address is changed by their ISP

Files:

- mail_p3.py: Small python 3 program to send an email, according to the specified parameters, with the ip passed as a parameter on the email body.
- mail_p2.py: The same program but in python 2.
- check_ip.py: Python program to check if your public ip has changed.

## How does it work?

Depending on the python installation you have, you may use one mail program or another. The check_ip.py program is in python 2.

In the case of the python 2 program, the mail message is quite simpler, as I had some troubles with it.

The mail_p2.py and mail_p3.py programs take an ip address as a parameter, and then use the configuration hardcoded in the code to send an email. Note that the smtp configuration is done for a gmail account.

The check_ip.py program checks the public ip of your network, compares it with the ip read from a file "ip.txt", and if they differ it sends a mail using the mail_p2.py program mentioned before, passing the new ip as a parameter. If the ip hasn't changed, it will create a flag named "no_ip_changes".

The first time you may need to create the ip.txt file by yourself, although an example file is also available in the repository.

## dns update

As a last step in the check_ip.py program, I have added the call to the script updste_dns.sh, which connects to the cloudflare API and changes the corresponding A registry to update the dns.

This step is optional, you can remove it from the program, but if you use cloudflare as your dns provider you might find this useful.