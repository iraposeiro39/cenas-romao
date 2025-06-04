#!/bin/python3
# Sockets

import socket

s = socket.socket()
s.settimeout(1)

ip = "213.13.146.142" # sapo.pt

porta_inicial = int(input("Insira a porta inicial da rede: "))
porta_final = int(input("Insira a porta final da rede: "))

for port in range(porta_inicial, porta_final+1):
    resultado = s.connect_ex((ip, port))
    if resultado == 0:
        print(f"{port} - Aberta")
    else:
        print(f"{port} - Fechada")
    s.close()
    s = socket.socket()
    s.settimeout(1)
    
    pass
