import subprocess
import shlex
import os

cmd=shlex.split('dig +short myip.opendns.com @resolver1.opendns.com')
result = subprocess.check_output(cmd).strip('\n')

f=open("ip.txt", "r")
contents =f.read().strip('\n')
print(result)
print(contents)
is_same = (result == contents)
print(is_same)

if is_same == False:
    line = "python mail_p2.py \"" + result + "\"" 
    os.system(line)
    line_2 ="echo " + result + " > ip.txt"
    os.system(line_2)
else:
    os.system("touch no_ip_changes")