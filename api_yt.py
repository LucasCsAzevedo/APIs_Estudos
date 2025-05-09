'''
    Uma API é um lugar para disponibilizar recursos e/ou funcionalidades
    Para criar uma API precisamos:
    1. Objetivo - Criar um api que disponibiliza a consulta, criação, edição e exclusão de livros.
    2. URL base - localhost
    3. Endpoints (Quais funcionalidades):
        - localhost/livros (GET)
        - localhost/livros (POST) - Criar novos livros
        - localhost/livros/id (GET) - Pegar um livro específico
        - localhost/livros/id (PUT) - Alterar um livro
        - localhost/livros/id (DELETE) - Deletar um livro
    4. Quais recursos
        - Vamos disponibilizar livros
''' 

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id' : 1,
        'titulo' : 'Medico de Homens e de Almas',
        'autor' : 'Taylor Caldwell'
    },
    {
        'id' : 2,
        'titulo' : 'O Grande amigo de Deus',
        'autor' : 'Taylor Caldwell'
    },
    {
        'id' : 3,
        'titulo' : 'O Peregrino',
        'autor' : 'John Bunyan'
    }
]

# Consultar todos
@app.route('/livros', methods=['GET']) # Coloco o endpoint e o somente o método GET vai funcionar nessa função
def obter_livros(): # Para cada endpoint preciso criar uma função
    return jsonify(livros)

# Consultar (Id)
@app.route('/livros/<int:id>', methods=['GET'])
def consultar_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar um livro
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    alteracoes = request.get_json()
    for idx, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[idx].update(alteracoes)
            return jsonify(livro)

# Criar livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for idx, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[idx]
            
    return jsonify(livros)
        
        
app.run(port=5000, host='localhost', debug=True)