from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/get", methods=["GET"])
def get_current_time():
    current_time = datetime.now()
    return jsonify(current_time)


@app.route("/zsofi", methods=["ZSOFI"])
def request_zsofi():
    return jsonify("HTTP method ZSOFI works")


if __name__ == '__main__':
    app.run()
