#!/bin/python3
# Trabalhar com funcoes e crypto

from cryptography.fernet import Fernet


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

def encrypt_password(plain_text_password, key_file):
    f = Fernet(key_file)
    encrypted_pass = f.encrypt(plain_text_password.encode())
    print(f"Encryted password: {encrypted_pass}")
    pass

def decrypt_password(encrypted_password, key_file):
    f = Fernet(key_file)
    decrypted_password = f.decrypt(encrypted_password).decode()
    print(f"Decrypted password: {decrypted_password}")
    pass

if __name__ == "__main__":

    key = load_key()
    # password = input("Insira uma palavra-passe: ")

    # encrypt_password(password, key)

    texto_cifrado = input("Insira o texto cifrado: ")
    print("Nunca deu???")
    decrypt_password(texto_cifrado, key)
    pass