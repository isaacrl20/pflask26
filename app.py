from flask import Flask, render_template , request
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO


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
    dao = AlunoDAO()
    lista= dao.listar()
    return render_template('aluno/lista.html', lista_alunos=lista)

@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista_professor=lista)

@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista_turma=lista)

@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista_curso=lista)

@app.route('/saudacao')
def saudacao():
    return render_template('saudacao/saudacao.html', valor_recebido='Visitante')


@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html',valor_recebido = nome)

@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    dados = {'Usuário': usuario, 'Senha': senha}
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/desafio')
def desafio():
    return render_template('desafio/desafio.html', valor_recebido='desafiante')

@app.route('/atv', methods=['POST'])
def atv():
    nome = request.form['nome']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento']
    nome_mae = request.form['nome_mae']

    dados = {'nome': nome, 'cpf': cpf, 'nascimento' : nascimento, 'nome_mae' : nome_mae}
    return render_template('desafio/desafio.html', valor_recebido=dados)



if __name__ == '__main__':
    app.run(debug=True)

