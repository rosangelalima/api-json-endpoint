from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/guia', methods=['POST'])
def receive_json():
    data = request.get_json()

    # Processando os dados recebidos
    return jsonify({
        "status": "sucesso",
        "mensagem": "JSON recebido com sucesso",
        "dadosRecebidos": data
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

