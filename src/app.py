from flask import Flask, jsonify, request
#jsonify convierte un diccionario en un string de formato json
app = Flask(__name__)
# 1 METODO GET
# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return "<h1>Hello!</h1>"
# 1.1 METODO GET
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return jsonify(todos)
# 2 METODO POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)