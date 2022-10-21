from flask import Flask, jsonify, request

app = Flask(__name__)

times_nfl = [
    {
        'id': 1,
        'name': 'Seattle Seahawks',
        'city': 'Seattle'
    },
    {
        'id': 2,
        'name': 'Kansas City Chiefs',
        'city': 'Kansas City'
    },
    {
        'id': 3,
        'name': 'Tamba Bay Buccaneers',
        'city': 'Tamba'
    },        
]

#Consultar Todos
@app.route('/times',methods=['GET'])
def obter_times():
    return jsonify(times_nfl)

#Consultar Pro ID
@app.route('/times/<int:id>',methods=['GET'])
def obter_times_id(id):
    for times in times_nfl:
        if times.get('id') == id:
            return jsonify(times)

#Incluir Time
@app.route('/times',methods=['POST'])
def incluir_time():
    novo_time = request.get_json()
    times_nfl.append(novo_time)

    return jsonify(times_nfl)

#Editar Time Por ID
@app.route('/times/<int:id>',methods=['PUT'])
def editar_times_id(id):
    time_alterado = request.get_json()
    for indice,time in enumerate(times_nfl):
        if time.get('id') == id:
            times_nfl[indice].update(time_alterado)
            return jsonify(times_nfl[indice])

#Excluir Time
@app.route('/times/<int:id>',methods=['DELETE'])
def excluir_time(id):
    for indice, time in enumerate(times_nfl):
        if time.get('id') == id:
            del times_nfl[indice]

    return jsonify(times_nfl)

#Rodar
app.run(port=5000, host='localhost', debug=True)



