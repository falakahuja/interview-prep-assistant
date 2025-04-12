from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from flask import Flask, request, jsonify
from gemini_helper import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return "Interview Prep Assistant API is running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = generate_response(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
