from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key='minhachave'

class Usuario:
	def __init__(self,id, nome, senha, email):
		self.id=id
		self.nome=nome
		self.senha=senha
		self.email=email

usuario1 = Usuario(1,"felipe",'1234', "felipe@felipe.com.br")
usuario2 = Usuario(2,"joão",'12345', "joao@joao.com.br")

lista = [usuario1,usuario2]

@app.route('/')
def index():
	proxima = request.args.get('proxima')
	return render_template("index.html", proxima=proxima)

@app.route('/usuarios')
def usuarios():
	return render_template("usuariosTeste.html",meusUsuarios=lista,titulo='Lista de usuários')

@app.route('/novousuario')
def novousuario():
	if 'usuario_logado' not in session or session['usuario_logado']==None:
		return redirect(url_for('index', proxima=url_for('novousuario')))
	return render_template('novousuario.html')

@app.route('/criar', methods=['POST',])
def criar():
	nome = request.form['nome']
	senha = request.form['senha']
	email = request.form['email']
	#usuario = Usuario(id,nome,idade,sexo,senha,email)
	#lista.append(usuario)
	return redirect('/usuarios')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
	if request.form['usuario'] in lista:
		usuario = lista[request.form['usuario']]
		if usuario.senha == request.form['senha']:
			session['usuario_logado'] = usuario.nome
			proxima_pagina=request.form['proxima']
			return redirect(proxima_pagina)
	else:
		return redirect(url_for('index'))	

@app.route('/logout')
def logout():
	session['usuario_logado']=None
	return redirect(url_for('index'))

app.run(debug=True)
