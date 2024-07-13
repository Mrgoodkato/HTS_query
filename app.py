from flask import Flask
from main import *
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True)