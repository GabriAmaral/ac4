from flask import Flask

clientes = {
  1: {
    'nome': "Van Halen"
  },
  
  2: {
    'nome': "Buckethead"
  },
}

class Cliente():
    def buscarNome(id):
        cliente = clientes[id]
        
        return cliente