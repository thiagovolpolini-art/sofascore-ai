from openai import OpenAI
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

print("Iniciando IA...")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("Conectando banco...")

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

pergunta = input("Pergunta: ")

print("Buscando jogadores...")

cursor.execute("""
SELECT nome, gols
FROM jogadores
ORDER BY gols DESC
LIMIT 5
""")

dados = cursor.fetchall()

print("Dados encontrados:")
print(dados)

contexto = "\n".join([
    f"{nome}: {gols} gols"
    for nome, gols in dados
])

print("Enviando para IA...")

try:

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Você é um analista de futebol."
            },
            {
                "role": "user",
                "content": f"""
                Dados:
                {contexto}

                Pergunta:
                {pergunta}
                """
            }
        ],
        timeout=30
    )

    print("\nResposta:\n")
    print(resposta.choices[0].message.content)

except Exception as erro:
    print("\nERRO:")
    print(erro)