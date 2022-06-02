import os
import sys
import time
import urllib.request
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

from key import*


message=str(input('Insert a text message: '))
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
urllib.request.urlopen
message=message.encode()
f = Fernet(key)
message=f.encrypt(message)
message=str(message)
print("\nThe message is encrypted: "+message)
b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=IVBQI0LZTK2JEKO1&field1=0'+message)
print("\nThe message is encrypted and sent!")
print("Use the encryption code to decrypt the message.")


