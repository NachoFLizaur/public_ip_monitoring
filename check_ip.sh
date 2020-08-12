#!/bin/bash

#Script to get public ip and save it in a file.

cd /home/pi/public_ip_monitoring/ 

if [ -s "PUBLIC_IP" ]; then
	read -r old_public_ip < PUBLIC_IP;
else
	old_public_ip="";
fi

host myip.opendns.com resolver1.opendns.com | grep "has address" | awk -F' ' '{ print $4}' > PUBLIC_IP;

if [ -s "PUBLIC_IP" ]; then
	
	read -r public_ip < PUBLIC_IP;
	
	if [ "$old_public_ip" != "$public_ip" ]; then
	
		python mail_p2.py $public_ip
		echo " DONE! "
	fi
else
	echo " ERROR: CANT GET PUBLIC IP "
fi
