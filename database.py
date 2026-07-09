import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "players.db")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jogadores (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome TEXT,

    time TEXT,

    nota REAL,

    gols INTEGER

)
""")

conn.commit()

print("Tabela criada com sucesso!")