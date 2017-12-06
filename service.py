from flask import Flask, request, jsonify
from predictor import Predictor

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def mbti_test():
    data = request.get_json(force=True)
    text = data['text']
    
    p = Predictor()
    mbti = p.run(text)
    
    return jsonify(results=mbti)

if __name__ == '__main__':
    app.run(port=3000, debug=True)