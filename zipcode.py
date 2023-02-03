from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/zip_code", methods=["GET"])
def get_zipCode():
    zip_code = 94537 # Hardcoded value
    return jsonify({"zip_code": zip_code})

if __name__ == "__main__":
    app.run(debug=True)