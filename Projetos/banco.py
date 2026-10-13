import sqlite3

def conectar():
    conexao = sqlite3.connect("produtos.db")

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)

    return conexao