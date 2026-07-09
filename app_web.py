from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "players.db")

@app.route("/", methods=["GET", "POST"])
def home():

    resultados = []
    titulo = "Pesquise uma estatística"

    if request.method == "POST":

        pergunta = request.form["pergunta"].lower()

        conn = sqlite3.connect(db_path)

        cursor = conn.cursor()

        # MAIS GOLS

        if (
            "gols" in pergunta
            or "artilheiro" in pergunta
            or "mais gols" in pergunta
        ):

            titulo = "🏆 Artilheiros"

            cursor.execute("""
            SELECT nome, time, gols
            FROM jogadores
            ORDER BY gols DESC
            LIMIT 10
            """)

            resultados = cursor.fetchall()

        # MELHORES NOTAS

        elif (
            "nota" in pergunta
            or "melhor jogador" in pergunta
            or "maior nota" in pergunta
        ):

            titulo = "⭐ Melhores Jogadores"

            cursor.execute("""
            SELECT nome, time, nota
            FROM jogadores
            ORDER BY nota DESC
            LIMIT 10
            """)

            resultados = cursor.fetchall()

        conn.close()

        print(resultados)

    return render_template(
        "index.html",
        resultados=resultados,
        titulo=titulo
    )

if __name__ == "__main__":
    app.run(debug=True)