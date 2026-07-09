import sqlite3

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

pergunta = input("Pergunta: ").lower()

# MAIOR NOTA
if "maior nota" in pergunta:

    cursor.execute("""
    SELECT nome, time, nota
    FROM jogadores
    ORDER BY nota DESC
    LIMIT 5
    """)

    jogadores = cursor.fetchall()

    print("\nTOP JOGADORES:\n")

    for jogador in jogadores:

        nome = jogador[0]
        time = jogador[1]
        nota = jogador[2]

        print(f"{nome} | {time} | Nota: {nota}")

# TOP JOGADORES
elif "top jogadores" in pergunta:

    cursor.execute("""
    SELECT nome, time, nota
    FROM jogadores
    ORDER BY nota DESC
    LIMIT 10
    """)

    jogadores = cursor.fetchall()

    print("\nRANKING:\n")

    for jogador in jogadores:

        nome = jogador[0]
        time = jogador[1]
        nota = jogador[2]

        print(f"{nome} | {time} | Nota: {nota}")

else:
    print("Pergunta não reconhecida.")