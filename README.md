# ⚽ Sofascore AI

![Dashboard do projeto](assets/dashboard.png)

Sistema web de análise de jogadores da Premier League utilizando dados do Sofascore.

## 🚀 Tecnologias utilizadas

- Python
- Flask
- SQLite
- Playwright
- HTML
- CSS

## 📊 Funcionalidades

- Coleta de dados do Sofascore
- Armazenamento em banco SQLite
- Ranking de artilheiros
- Ranking de melhores notas
- Interface web para consultas
- Dashboard simples e responsivo

## 🖥️ Como executar

Clone o projeto:

```bash
git clone https://github.com/thiagovolpolini-art/sofascore-ai.git
```

Entre na pasta:

```bash
cd sofascore-ai
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale os navegadores do Playwright:

```bash
python -m playwright install
```

Crie o banco:

```bash
python database.py
```

Colete os dados:

```bash
python playwright_test.py
```

Execute o sistema:

```bash
python app_web.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

## 📌 Exemplos de perguntas

```text
quem tem mais gols
```

```text
melhor jogador
```

```text
maior nota
```

## 👨‍💻 Autor

Desenvolvido por Thiago Volpolini.