from playwright.sync_api import sync_playwright
import json
import sqlite3
import os

# GARANTE CAMINHO ABSOLUTO
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "players.db")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

url = "https://www.sofascore.com/api/v1/unique-tournament/17/season/76986/top-players/overall"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(url)

    conteudo = page.text_content("body")

    dados = json.loads(conteudo)

    jogadores = dados["topPlayers"]["rating"]

    print("\nSALVANDO JOGADORES...\n")

    for jogador in jogadores:

        nome = jogador["player"]["name"]

        time = jogador["team"]["name"]

        nota = jogador["statistics"]["rating"]

        gols = jogador["statistics"].get("goals") or 0

        cursor.execute("""
        INSERT INTO jogadores
        (nome, time, nota, gols)
        VALUES (?, ?, ?, ?)
        """, (
            nome,
            time,
            nota,
            gols
        ))

        print(f"{nome} salvo!")

    conn.commit()

    browser.close()

print("\nTodos jogadores salvos!")