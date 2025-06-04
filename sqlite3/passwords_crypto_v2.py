#!/bin/python3
# Trabalhar com funcoes e crypto

from cryptography.fernet import Fernet

import sqlite3

# Cenas da BD
nomeBD = 'BaseDeDados.db'

global conn
conn = sqlite3.connect(nomeBD)
global c
c = conn.cursor()


def generate_key(file):
    key = Fernet.generate_key()
    with open(file, "wb") as f:
        f.write(key)
    pass

def load_key():
    with open("secret.key", "rb") as f:
        key = f.read()
        return key
    pass

def encrypt_password(key_file):
    f = Fernet(key_file)

    # Inserir dados
    username = input("Inserir novo username: ")
    plain_text_password = input("Nova pass (PLAINTEXT): ")
    
    encrypted_pass = f.encrypt(plain_text_password.encode())
    print(f"Encryted password: {encrypted_pass}")

    # Inserir na BD
    sql = "INSERT INTO helldivers (username, password) VALUES (?, ?);"
    dados = (username, encrypted_pass)
    c.execute(sql, dados)
    conn.commit()
    print("Password guardada na base de dedos com success")
    pass

def decrypt_password(key_file):
    sql = "SELECT id, username FROM helldivers;"
    c.execute(sql)
    resultado = c.fetchall()

    # Mostrar todos os users da bd
    for i in resultado:
        print(i)

    # Query ao user e à base de dados
    id_user = input("Selecionar Utilizador (id): ")
    sql = "SELECT password FROM helldivers WHERE id = ?"
    dados = (id_user)
    c.execute(sql, dados)
    resultado = c.fetchall()[0][0]
    print(f"Pass: {resultado}")

    # Desencriptar a pass
    while True:
        opt = input("\nDeseja a pass desencriptada? (y/n): ")
        match opt:
            case "y":
                break
            case "n":
                return
            case _:
                print("Opção Inválida")
    
    f = Fernet(key_file)
    decrypted_password = f.decrypt(resultado).decode()
    print(f"\nDecrypted password: {decrypted_password}")
    pass

def main():
    while True:
        print("\n== Menu Pass crypto ==")
        print("1 - Gerar Chave de crypto")
        print("2 - Registar novo username e pass")
        print("3 - Ler passwords")
        print("4 - Sair")
        opt = int(input("> "))
        
        match opt:
            case 1:
                generate_key("secret.key")
                print(f"Pass Criada:\n{load_key()}")
            case 2:
                key = load_key()
                encrypt_password(key)
            case 3:
                key = load_key()
                decrypt_password(key)
            case 4:
                print("Bye!")
                break

            case _:
                print("Valor Inválido")


if __name__ == "__main__":
    main()




    # generate_key()
    # key = load_key()
    # password = input("Insira uma palavra-passe: ")

    # encrypt_password(password, key)

    # texto_cifrado = input("Insira o texto cifrado: ")
    # print("Nunca deu???")
    # decrypt_password(texto_cifrado, key)
    # pass