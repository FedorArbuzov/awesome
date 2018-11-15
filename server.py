from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


import signal
signal.signal(signal.SIGTERM, lambda *args: print('term', *args))
signal.signal(signal.SIGINT, lambda *args: print('int', *args))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
