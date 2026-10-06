import sqlite3

conexao = sqlite3.connect("meu_banco.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
)
""")

conexao.commit()

print("Tabela Criada")