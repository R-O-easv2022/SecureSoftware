import os
import sys
import time
import requests
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass




usr = getpass.getpass(prompt='Enter Username? ')
pss = getpass.getpass(prompt='Enter password? ')

if (usr.lower() == 'admin') & (pss.lower() == 'adminpss') :
    
	message=requests.get("https://thingspeak.com/channels/1704380/field/1")
	message=message.json()['feeds'][-1]['field1']
	add_password = input("Encryption code: ") 
	psw = add_password.encode()
	salt = b'salt_'
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=100000,
		backend=default_backend()
	)
	key = base64.urlsafe_b64encode(kdf.derive(psw))
	f=Fernet(key)
	print("\nThe encrypted message that received is:\n\n"+message)
	message=message[2:-1]
	message=bytes(message,'utf-8')
	message=f.decrypt(message)
	print("\nThe sent message is: \n\n"+str(message)[2:-1])

else:
    print('PASSWORD IS INCORRECT!')
    
    