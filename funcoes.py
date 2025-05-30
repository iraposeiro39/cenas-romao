#!/bin/python3

## Importa todas as funções
from tretas import *

## Importa apenas uma função
# from tretas import funcao1

v = 100

def funcao1(arg1):
    valor_modificado = arg1 * 2
    valor_original = arg1

    return valor_modificado, valor_original
    pass

modificado, original = funcao1(v)

print(f"Modificado: {modificado}")
print(f"Original: {original}")

funcao2()