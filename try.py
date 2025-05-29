#!/bin/python3
import os


try:
    print("tretas")
    f = open("badjoras.txt")

except FileNotFoundError:
    print("Não há badjoras para ninguém")
    os.system("touch badjoras.txt")

except Exception as e:
    print(f"ERROR: {e}")
finally:
    print("Isto executa sempre!")


# ==========================================================================================================

n = 0

if n == 0:
    raise Exception("Isto nao pode ser zero")
if type(n) is not int:
    raise Exception("A variavel N precisa de ser um número")