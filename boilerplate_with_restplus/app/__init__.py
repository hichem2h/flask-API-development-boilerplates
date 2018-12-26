from flask import Flask

app = Flask(__name__)


@app.route('/')
def health():
    return 'OK'


from api import bp as api_bp

app.register_blueprint(api_bp)