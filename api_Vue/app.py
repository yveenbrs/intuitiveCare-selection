from flask import Flask, request, jsonify
from flask_cors import CORS

from utils import read_csv

# 1. Gera conexão com o flask usando o CORS
app = Flask(__name__)
CORS(app)

# 2. Declara variável de ambiente e chama função para leitura
CSV_FILE = 'csv/Relatorio_cadop.csv'
data_list = read_csv(CSV_FILE)

# 3. Chama o método GET
@app.route("/search", methods=["GET"])
def search_operadora():
    term = request.args.get("term", "").strip().lower()
    
    if not term:
        return jsonify({"error": "Não foi realizado nenhuma requisição."}), 400
    
    matching_results = [data for data in data_list if term in data[2].lower()]

    seen_operadoras = set()
    final_results = []

    for data in matching_results:
        operadora_name = data[2].strip().lower()
        if operadora_name not in seen_operadoras:
            final_results.append(data)
            seen_operadoras.add(operadora_name)

    if not final_results:
        return jsonify({"error": "Nenhuma operadora localizada!"}), 404

    return jsonify({"results": final_results})

if __name__ == "__main__":
    app.run(debug=True)
