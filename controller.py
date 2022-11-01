from flask import Flask, jsonify
from model import Cliente

app = Flask(__name__)

@app.route('/buscarNome', methods=["GET"])
def consultar():
    return jsonify(Cliente.buscarNome(2))

if __name__ == '__main__':
  app.run(debug=True)