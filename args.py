#!/bin/python3
import argparse
import os

cmd_ping = "ping -c 2 "

parser = argparse.ArgumentParser(description="Script para fazer ping")

parser.add_argument('--address', '-a', type=str, required=True, help="Endereço de IP a conectar")
parser.add_argument('--count', '-c', type=str, required=True, help="Quantidade de requests")
args = parser.parse_args()

print(args.address)
print(args.count)

# Com format
cmd_ping = "ping -c {} {}".format(args.count, args.address)
# Com f flag
cmd_ping = (f"ping -c {args.count} {args.address}")
print(cmd_ping)


resposta = os.popen( cmd_ping ).read()
print(resposta)


if "ttl" in resposta:
    # Com format
    print("[{}] Ligado".format(args.address))
    # Com f flag
    print(f"[{args.address}] Ligado (com f flag)")


if "ttl" in resposta == 128:
    print("Linux!")
elif "ttl" in resposta == 64:
    print("Windows!")







'''
while True:
    test = input("Inserir endereco de IP: ")
    print(">>> endereco {}".format(test))


    if test == "exit":
        break
    else:
        comando = cmd_ping + test
        print("Fazer ping")
        #print( comando )
        resposta = os.system(comando)
        print(resposta)
    pass
'''