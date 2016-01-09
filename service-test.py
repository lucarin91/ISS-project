#!/bin/python3

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/', methods=['POST'])
def parse_request():
    data = request.get_data()
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True)

