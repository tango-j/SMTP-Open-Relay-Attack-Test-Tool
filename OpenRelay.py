import socket
import smtplib
from smtplib import *

IP = raw_input("Enter Ip address: ")
Port = raw_input("Enter Port Number: ")

X = raw_input("From: ")
Y = raw_input("TO: ")

s = socket.socket()
s.connect((IP,int(Port)))
socket.setdefaulttimeout(3)

ans = s.recv(1024)


if ("220" in ans):
    print "\n[+]Port" + " " + str(Port) + " " + "open on the target system\n"
    smtpserver = smtplib.SMTP(IP,int(Port))
    r = smtpserver.docmd("Mail From:",X)
    a = str(r)
    if ("250" in a):
        r = smtpserver.docmd("RCPT TO:",Y)
        a = str(r)
        if ("250" in a):
            
            print "[+]The target system seems vulenarble to Open relay attack"

        else:
            print "[-]The target system is not vulnerable to Open relay attack "
        
    
else:
    print "[-]Port is closed/Filtered"
