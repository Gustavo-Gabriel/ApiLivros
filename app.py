# API é um lugar para disponibilizar recursos e/ou funcionalidaes

# Para Criar APis precisamos de pelos menos 4 etapas
# 1 - Objetivo - Criar uma API que disponibiliza o CRUD de livros
# 2 - URL Base - localhost.com por enquanto gratuito
# 3 - Endpoint - 
    # localhost/livros (GET)
    # localhost/livros/id (GET)
    # localhost/livros/id (PUT)
    # localhost/livros/id (DELETE)
# 4 - Quais Recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Entre Nós',
        'autor': 'Gustavo'
    },

    {
        'id': 2,
        'titulo': 'Entre Nós 2',
        'autor': 'Andrya'
    },

    {
        'id': 3,
        'titulo': 'Entre Nós 3',
        'autor': 'Gustavo e Andrya'
    }
]

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultr (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return livro

# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()

    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Incluir novo livro
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=8000, host='localhost', debug=True)
