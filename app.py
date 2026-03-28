from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "API de Cotação de Moedas está online!"

@app.route("/cotacao/<moeda>")
def cotacao(moeda):
    moeda = moeda.upper()

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    resposta = requests.get(url)

    if resposta.status_code != 200:
        return jsonify({"erro": "Erro ao buscar cotação"}), 500

    dados = resposta.json()

    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)
