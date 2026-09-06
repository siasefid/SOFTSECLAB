from flask import Flask, jsonify, request

from src.calculator import Calculator

app = Flask(__name__)

calculator = Calculator()


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello World"}), 200


@app.route("/calc", methods=["POST"])
def calc():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    if "expression" not in data:
        return jsonify({"error": "expression is required"}), 400

    expression = data["expression"]

    if not isinstance(expression, str):
        return jsonify({"error": "expression must be a string"}), 400

    try:
        result = calculator.calc(expression)
        return jsonify({"result": result}), 200

    except ValueError:
        return jsonify({"error": "invalid expression"}), 400