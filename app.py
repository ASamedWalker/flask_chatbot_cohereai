from flask import Flask
import cohere

app = Flask(__name__)

co = cohere.Client()

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/item/<destination>')
def text_completion():
