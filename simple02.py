from dotenv import load_dotenv
# load_dotenv()
load_dotenv(verbose=True)

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")  # curl -v http://127.0.0.1:5000/
def hello():
    return jsonify({"about": "Hello World!"})


if __name__ == '__main__':
    app.run(debug=True)
