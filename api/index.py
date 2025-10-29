from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    secret_value = os.environ.get("MY_SECRET", "No secret configured")
    return jsonify({
        "message": "Hello, Flask API is working on Vercel!",
        "secret": secret_value
    })

if __name__ == "__main__":
    app.run()
