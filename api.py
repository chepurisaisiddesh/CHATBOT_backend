# src/api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import text_gen_pipeline  # Import your shared pipeline

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    if prompt:
        output = text_gen_pipeline(prompt)
        return jsonify({'response': output[0]['generated_text']})
    return jsonify({'response': ''})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

