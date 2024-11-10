## app.py
from flask import Flask, request, jsonify
from utils import load_data
from subgraph_mining import SubgraphMining
from visualization import Visualization

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Subgraph Mining Application!"

@app.route('/mine', methods=['POST'])
def mine_subgraphs():
    """
    Endpoint to mine subgraphs based on provided data and parameters.
    Expects a JSON payload with 'file_path' and 'parameters'.
    """
    content = request.json
    file_path = content.get('file_path', '')
    parameters = content.get('parameters', {})

    if not file_path:
        return jsonify({"error": "file_path is required"}), 400

    data = load_data(file_path)
    if not data:
        return jsonify({"error": "Failed to load data from provided file path"}), 400

    if 'nodes' not in data or 'edges' not in data:
        return jsonify({"error": "Data format is incorrect, missing 'nodes' or 'edges'"}), 400

    if not parameters:
        return jsonify({"error": "Failed to parse parameters or parameters are empty"}), 400

    subgraph_mining = SubgraphMining()
    subgraphs = subgraph_mining.find_frequent_subgraphs(data, parameters)

    if not subgraphs:
        return jsonify({"message": "No frequent subgraphs found"}), 404

    visualization_html = Visualization.plot_subgraphs(subgraphs)
    if not visualization_html:
        return jsonify({"error": "Failed to generate visualizations for the subgraphs"}), 500

    return jsonify({"visualization": visualization_html}), 200

if __name__ == '__main__':
    app.run(debug=True)
