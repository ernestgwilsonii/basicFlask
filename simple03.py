from dotenv import load_dotenv
# load_dotenv()
load_dotenv(verbose=True)

from flask import Flask, jsonify, request

app = Flask(__name__)


# curl -X POST http://127.0.0.1:5000/ -H "Content-Type: application/json" -d '{"test":"Hello"}'
@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({"some_json": some_json}), 201
    else:
        return jsonify({"about": "Hello World!"})


# curl http://127.0.0.1:5000/multi/10
@app.route("/multi/<int:num>", methods=['GET'])
def get_multipli10(num):
    return jsonify({"result": num*10})


if __name__ == '__main__':
    app.run(debug=True)
