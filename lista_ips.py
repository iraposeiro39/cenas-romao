#!/bin/python3

lista_ips = []
lista_pequena = []

ip = "192.168.1"

for i in range(1,256):
    ip_full = (f"{ip}.{i}")
    lista_ips.append(ip_full)

print(lista_ips)

# Copiar indexes, se uma for alterada, a outra muda também
lista_ips = lista_pequena

# Copiar lista completamente
lista_ips = lista_pequena.copy()