import sys, os
from flask import Flask, render_template, request
sys.path.append(os.path.abspath('main'))
from main import query_hts_db, query_string_db
from main.utils.util_functions import processTextAreaInput

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('home.html.j2', title='Enter query')

@app.route('/process_query')
def process_query():
    query = processTextAreaInput(request.args['user_input'])
    query_result = query_hts_db.queryHTSNumber(query['query_list'], testing=True)
    return render_template('query_results.html.j2', query_result=query_result)

@app.route('/process_file_query')
def process_file_query():
    
    return 'Hello there'

if __name__ == '__main__':
    app.run(debug=True)