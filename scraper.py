import sqlite3

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

jogadores = [
    ("Haaland", "Manchester City", 27, 5, 7.8),
    ("Salah", "Liverpool", 24, 11, 7.7),
    ("Son", "Tottenham", 19, 8, 7.5),
]

for jogador in jogadores:
    cursor.execute("""
    INSERT INTO jogadores
    (nome, time, gols, assistencias, nota)
    VALUES (?, ?, ?, ?, ?)
    """, jogador)

conn.commit()

print("Jogadores inseridos!")