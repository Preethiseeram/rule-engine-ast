from flask import Flask, request, jsonify
from rule_ast import create_rule, evaluate_rule
from db import store_rule, get_rules

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json['rule']
    store_rule(rule_string)
    return jsonify({"message": "Rule stored successfully"}), 201

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_string = request.json['rule']
    data = request.json['data']
    ast = create_rule(rule_string)
    result = evaluate_rule(ast, data)
    return jsonify({"result": result})

@app.route('/rules', methods=['GET'])
def get_rules_api():
    rules = get_rules()
    return jsonify(rules)

if __name__ == "_main_":
    app.run(debug=True)