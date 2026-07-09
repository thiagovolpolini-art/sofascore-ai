import sqlite3

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

print("\n=== SOFASCORE AI ===\n")

pergunta = input("Pergunta: ").lower()

# ====================================
# MAIOR NOTA
# ====================================

if any(palavra in pergunta for palavra in [
    "maior nota",
    "melhor jogador",
    "melhores notas",
    "top nota"
]):

    cursor.execute("""
    SELECT nome, time, nota
    FROM jogadores
    ORDER BY nota DESC
    LIMIT 5
    """)

    jogadores = cursor.fetchall()

    print("\nTOP NOTAS:\n")

    for jogador in jogadores:

        nome = jogador[0]
        time = jogador[1]
        nota = jogador[2]

        print(f"{nome} | {time} | Nota: {nota}")

# ====================================
# TOP JOGADORES
# ====================================

elif "top jogadores" in pergunta:

    cursor.execute("""
    SELECT nome, time, nota
    FROM jogadores
    ORDER BY nota DESC
    LIMIT 10
    """)

    jogadores = cursor.fetchall()

    print("\nTOP JOGADORES:\n")

    for jogador in jogadores:

        nome = jogador[0]
        time = jogador[1]
        nota = jogador[2]

        print(f"{nome} | {time} | Nota: {nota}")

# ====================================
# BUSCAR JOGADOR
# ====================================

elif "jogador" in pergunta:

    nome_jogador = input("Nome do jogador: ")

    cursor.execute("""
    SELECT nome, time, nota
    FROM jogadores
    WHERE nome LIKE ?
    """, (f"%{nome_jogador}%",))

    jogadores = cursor.fetchall()

    print("\nRESULTADO:\n")

    for jogador in jogadores:

        nome = jogador[0]
        time = jogador[1]
        nota = jogador[2]

        print(f"{nome} | {time} | Nota: {nota}")

# ====================================
# MAIS GOLS
# ====================================

elif any(palavra in pergunta for palavra in [
    "gols",
    "artilheiro",
    "mais gols",
    "quem fez mais gols"
]):

    cursor.execute("""
    SELECT nome, time, gols
    FROM jogadores
    ORDER BY gols DESC
    LIMIT 10
    """)

    jogadores = cursor.fetchall()

    print("\nARTILHEIROS:\n")

    for jogador in jogadores:

        nome = jogador[0]
        time = jogador[1]
        gols = jogador[2]

        print(f"{nome} | {time} | Gols: {gols}")

# ====================================
# NÃO RECONHECIDA
# ====================================

else:
    print("\nPergunta não reconhecida.")