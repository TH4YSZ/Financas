from flask import Flask, jsonify, request 
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

try:
    open('despesas.csv', 'x')
    with open("despesas.csv", "a", encoding='utf-8') as arquivo:
         arquivo.write("ID,TAREFA\n") 
except Exception as e:
    pass

@app.route("/")
def homepage():
  return("API ONLINE")

############### GET ########################
@app.route("/list", methods=['GET'])
def listarDespesa():    
    despesas = pd.read_csv('despesas.csv', encoding='utf-8')
    despesas = despesas.to_dict('records')    
    return jsonify(despesas)

############### POST ########################
@app.route("/add", methods=['POST'])
def addDespesa():
    item = request.json 
    despesas = pd.read_csv('despesas.csv', encoding='utf-8')
    despesas = despesas.to_dict('records') 
    id = len(despesas) + 1
    with open("despesas.csv", "a", encoding='utf-8') as arquivo:
         arquivo.write(f"{id},{item['despesa']}\n")    

    despesas = pd.read_csv('despesas.csv')
    despesas = despesas.to_dict('records')        
    return jsonify(despesas)

############### UPDATE ########################
@app.route("/update/<int:id>", methods=['PUT'])
def updateDespesa(id):
    item = request.json  
    despesas = pd.read_csv('despesas.csv', encoding='utf-8')
    despesas = despesas.to_dict('records') 
    with open("despesas.csv", "a", encoding='utf-8') as arquivo:
        arquivo.write("ID,\n") 
        for despesas in despesas:
            if despesas['ID'] != id:
                arquivo.write(f"{despesas['ID']},{despesas['DESPESAS']}\n") 
            else:
                arquivo.write(f"{id},{item['|Despesas']}\n") 
    despesas = pd.read_csv('despesas.csv', encoding='utf-8')
    despesas = despesas.to_dict('records')        
    return jsonify(despesas)

############### DELETE ########################
@app.route("/delete", methods=['DELETE'])
def deleteDespesa():
    data = request.json
    id = data.get('id')
    if id is None:
        return jsonify({"error": "ID da despesa não fornecido"}), 400
    despesas = pd.read_csv('despesas.csv', encoding='utf-8')
    if id not in despesas['ID'].values:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    despesas = despesas.drop(despesas[despesas['ID'] == id].index)
    despesas['ID'] = range(1, len(despesas) + 1)
    despesas.to_csv('despesas.csv', index=False)
    return jsonify(despesas.to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")