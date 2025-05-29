#!/bin/python3
import os

lista = []

ip = "192.168.1"

print
for i in range(1,256):
    # Comando
    resposta = os.popen(f"ping -c 1 {ip}.{i}").read()
    print(f"{ip}.{i}...")
    # Verificar se tá on
    if "ttl" in resposta:
        print(f"[{ip}.{i}] Ligado")
        lista.append(f"{ip}.{i}")

print("\n== IPs detectados ==")
for i in range(len(lista)):
    print(lista[i])