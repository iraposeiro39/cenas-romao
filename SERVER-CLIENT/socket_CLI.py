#!/bin/python3
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "localhost"
porto = 5000

s.connect((ip, porto))

s.send(b"This is a message for the server")
msg = s.recv(1024)

print("Mensagem recebida do servidor: ", msg.decode())
