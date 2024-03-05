from flask import Flask, jsonify

helloApp = Flask(__name__)


@helloApp.route("/")
def hello():
    return "hello, flask"


@helloApp.route("/json")
def json():
    return jsonify({"name": "zenos", "age": 18})

@helloApp.route("/json2")
def json2():
    return {"name": "zenos", "age1": 18}

if __name__ == '__main__':
    helloApp.run(port=8080)