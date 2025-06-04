#!/bin/python3
# Sockets servidor

import socket
ip = "localhost"
porta = 5000

print("A iniciar servidor!")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.SOCK_STREAM --> TCP
# socket.SOCK_DGRAM ---> UDP

s.bind((ip, porta))
s.listen(20)