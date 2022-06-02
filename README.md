# SecureSoftware
mini-project
This mini-project is part of Secure Software course, and has been done by one student Rolan Ossi. 
The system provides end-to-end privacy for encrypting messages between sender and reciever. In addition, a key maganement has been added to the system that provides extra privacy and encryption by using Deffie-Hellman algorithm.
The system start from send.py
Firstly, the system implements the Deffie-Hellman algorithm by asking for lock the algorithm by putting key 1, then the algorithm moves to the receiver and asks lock the algorithm by key 2 from receiver, then the algorithm back to sender to unlock the system and travel again to receiver to unlock the system by its own key.
Secondlly, the system asks to insert the text message that sender will send it to receiver. After that, the system asks to add an encryption code in order t secure the message.
The message travel through api that already created by thingspeak in order to receive it to the receiver. Then the message will encrypt.
Thirdlly, the message arrives to receiver by api, and here another securety layer has been implemented. The system asks for a useername and password in order to acces to the message.
Once, username and password are correct, the system asks for the encryption code that sender already putted.
When the encryption code is inserted, then the encrypted message will decrypt and the message will appear for receiver.

