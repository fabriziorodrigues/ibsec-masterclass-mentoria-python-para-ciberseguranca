import sqlite3

def criar_conexao():
    conn = sqlite3.connect('exemplo.db')
    return conn

def criar_tabela():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def inserir_usuario(nome, email):
    conn = criar_conexao()
    cursor = conn.cursor()
    # Uso de consulta parametrizada para prevenir injeção de SQL
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()

def buscar_usuario(email):
    conn = criar_conexao()
    cursor = conn.cursor()
    # Uso de consulta parametrizada para prevenir injeção de SQL
    cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

# Criar tabela
criar_tabela()

# Inserir usuário
inserir_usuario('Alice', 'alice@example.com')

# Buscar usuário
usuario = buscar_usuario('alice@example.com')
print(usuario)
