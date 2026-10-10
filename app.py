import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return jsonify(
        message="Hello from my DevOps demo app!",
        version=VERSION,
        host=socket.gethostname(),  # shows the container ID when run in Docker
    )


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
