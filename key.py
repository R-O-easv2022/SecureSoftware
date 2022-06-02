
import os
import sys

p=int(input('INT1: ')) #this is key p
q = int(input("INT2: "))     #this is key q

Alice_key  = int(input("Sender Key:"))
Bob_key  = int(input("Reciever Key:"))

alice = p**Alice_key % q
bob = p**Bob_key % q

Alice = bob**Alice_key % q
Bob = alice*Bob_key % q
print (Alice)
print(Bob)

# print (sendMe)