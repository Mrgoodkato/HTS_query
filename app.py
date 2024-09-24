import sys, os
from flask import Flask, render_template
sys.path.append(os.path.abspath('main'))
from main import query_hts_db, query_string_db


app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('home.html.j2', title='Hello there')

if __name__ == '__main__':
    app.run(debug=True)