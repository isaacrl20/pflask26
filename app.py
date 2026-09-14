from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/aluno')
def listar_aluno():
    # Conecta ao banco de dados
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Executa consulta SQL
    cursor.execute('SELECT id, nome, idade, cidade FROM aluno')
    # Obtém todos os registros
    lista = cursor.fetchall()
    # Fecha conexão
    conn.close()
    return render_template('aluno/lista.html', lista_alunos=lista)

@app.route('/professor')
def listar_professor():
    # Conecta ao banco de dados
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Executa consulta SQL
    cursor.execute('SELECT id, nome, idade, cidade FROM professor')
    # Obtém todos os registros
    lista = cursor.fetchall()
    # Fecha conexão
    conn.close()
    return render_template('professor/lista.html', lista_professor=lista)

@app.route('/turma')
def listar_turma():
    # Conecta ao banco de dados
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Executa consulta SQL
    cursor.execute('SELECT id, nome, turma FROM turma')
    # Obtém todos os registros
    lista = cursor.fetchall()
    # Fecha conexão
    conn.close()
    return render_template('turma/lista.html', lista_turma=lista)









if __name__ == '__main__':
    app.run(debug=True)

