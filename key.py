
import os
import sys

key1=int(input('Key 1: ')) #this is key p
key2 = int(input("Key 2: "))     #this is key q

key_send  = int(input("Sender Key:"))
key_receive  = int(input("Reciever Key:"))

send = key1**key_send % key2
receive = key1**key_receive % key2

Sender = receive**key_send % key2
Receiver = send*key_receive % key2
print (Sender)
print(Receiver)

# print (sendMe)