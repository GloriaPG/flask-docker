from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)


@app.route('/hola/')
def nsg_detail():
    return "Hola"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')

