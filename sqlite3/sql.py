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

conn.executescript(sql)
conn.commit()