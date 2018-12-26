from flask import Flask

app = Flask(__name__)


@app.route('/')
def health():
    return 'OK'


from namespace1 import bp as ns1

app.register_blueprint(ns1)
