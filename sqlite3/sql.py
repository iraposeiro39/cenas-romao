#!/bin/python3
import sqlite3

nomeBD = 'BaseDeDados.db'

global conn
conn = sqlite3.connect(nomeBD)
c = conn.cursor()

sql = """
CREATE TABLE helldivers (
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
"""
try:
    conn.executescript(sql)
    conn.commit()
except:
    print("Tabela já existe!")

# Inserir dados para a BD
sql = """
INSERT INTO helldivers (username, password)
VALUES("DanielMaia", "User_!23");
"""

# conn.executescript(sql)
# conn.commit()

# username = input("Insert Username: ")
# password = input("Insert Password: ")

### CODIGO DE MERDA
# sql = "INSERT INTO helldivers (username, password) VALUES('" + username + "', '" + password + "');"
# print(sql)

## Exemplo de SQL injection
# Insert Username: Ciber 
# Insert Password: HAHA ARDEU'); DROP TABLE helldivers;
## Output:
# INSERT INTO helldivers (username, password) VALUES('Ciber', 'HAHA ARDEU'); DROP TABLE helldivers;');

## Exemplo com flag f (é mau na mesma)
# sql = (f"""
# INSERT INTO helldivers (username, password)
# VALUES("{username}", "{password}");
# """)

### CODIGO OLRIGHT
# sql = "INSERT INTO helldivers (username, password) VALUES(?, ?);"
# dados = (username, password)
# c.execute(sql, dados)
# conn.commit()

# Ele vai aceitar o comando SQL como texto


### SELECTS e afins
## Á pedreiro
sql = "SELECT * FROM helldivers;"
c.execute(sql)
resultado = c.fetchall()

for registo in resultado:
    print(registo[2])