from flask import Flask, jsonify, request

app = Flask(__name__)

items = {}

@app.route("/")
def home():
    return {
        "service": "Inventory Service",
        "status": "running"
    }

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    }), 200

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json

    items[data["id"]] = {
        "name": data["name"],
        "qty": data["qty"]
    }

    return jsonify(items[data["id"]]), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)