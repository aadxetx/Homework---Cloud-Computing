from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def get_weather():
    weather = None
    zipcode = request.args.get("zipcode")
    if zipcode == '94537':
        weather = "hot" 
    elif zipcode == '94557':
        weather = 'cold'
    else:
        print("wrong zipcode")
    return jsonify({"weather": weather})

if __name__ == "__main__":
    app.run(debug=True)