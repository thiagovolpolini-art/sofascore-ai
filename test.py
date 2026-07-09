import sqlite3

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM jogadores
""")

dados = cursor.fetchall()

for jogador in dados:
    print(jogador)