
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/guess', methods=['POST'])
def guess_number():
    data = request.get_json()
    guess = data['guess']
    target = data['target']
    if guess == target:
        return jsonify({"message": "おめでとうございます、あなたの推測は正解です!"})
    elif guess < target:
        return jsonify({"message": "もっと大きい数を推測してみてください"})
    else:
        return jsonify({"message": "もっと小さい数を推測してみてください"})

@app.route('/target', methods=['GET'])
def generate_target():
    start = 1
    end = 100
    target = random.randint(start, end)
    return jsonify({"target": target})

if __name__ == '__main__':
    app.run(debug=True)
