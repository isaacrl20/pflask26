from flask import Flask, render_template , request , redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO


app = Flask(__name__)
app.secret_key = "uma_chave_muito_secreta_e_unica"


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

@app.route('/aluno/form')  # rota formulário de aluno
def form_aluno():
    return render_template('aluno/form.html', aluno=None)

@app.route('/aluno/salvar/', methods=['POST'])  # Inserção
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    result = dao.salvar(id , nome , idade , cidade)
    if result['status']=='ok':
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result['mensagem'], "danger")
    return redirect('/aluno')


@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista_professor=lista)

@app.route('/professor/form')  # rota formulário de aluno
def form_professor():
    return render_template('professor/form.html', professor=None)

@app.route('/professor/salvar/', methods=['POST'])  # Inserção
def salvar_professor(id=None):
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    dao = ProfessorDAO()
    result = dao.salvar(id , nome , disciplina )
    if result['status']=='ok':
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result['mensagem'], "danger")
    return redirect('/professor')

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

@app.route('/curso/form')  # rota formulário de aluno
def form_curso():
    return render_template('curso/form.html', curso=None)

@app.route('/curso/salvar/', methods=['POST'])  # Inserção
def salvar_curso(id=None):
    nome_curso = request.form['nome']
    duracao = request.form['duracao']
    dao = CursoDAO()
    result = dao.salvar(id , nome_curso , duracao )
    if result['status']=='ok':
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result['mensagem'], "danger")
    return redirect('/curso')

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

