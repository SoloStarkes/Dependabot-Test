from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from the outdated-dependencies API!",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)
