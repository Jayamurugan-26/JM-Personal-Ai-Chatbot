from flask import Flask, request, jsonify
from flask_cors import CORS
from bot import ask_bot
import os

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Question is required"}), 400
    question = data["question"].strip()
    if not question:
        return jsonify({"error": "Empty question"}), 400
    answer = ask_bot(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
