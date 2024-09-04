from flask import Flask, jsonify, request
#jsonify convierte un diccionario en un string de formato json
app = Flask(__name__)

# variable global que contiene una lista
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# 2 METODO POST
@app.route('/todos', methods=['POST'])
def add_new_todo():

    # capturando el body, pasandolo a formato json y guardandolo en una variable
    body = request.json
    # imprime cada vez que agreguemos un body, el string + body
    print("Incoming request with the following body", body)
    
    # Verifica el tipo de dato de body, en este caso lista
    if isinstance(body, list):
    # se añade la lista del cuerpo a la lista de todos
        todos.extend(body)
    else:
    # se añade un objeto a la lista
        todos.append(body)
    
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)

# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)