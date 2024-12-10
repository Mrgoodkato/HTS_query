import sys, os
from openpyxl import Workbook, load_workbook
from flask import Flask, render_template, request, jsonify
sys.path.append(os.path.abspath('main'))
from main import query_hts_db, query_string_db
from main.utils.util_functions import processTextAreaInput

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html.j2', title='Enter query')

@app.route('/process_query', methods=['POST'])
def process_query():

    user_input = request.form.getlist('user_input') or request.form.getlist('user_input_manual')
   
    query_string = '\n'.join(user_input)
    query = processTextAreaInput(query_string)
    errors = query['errors']
    query_result = query_hts_db.queryHTSNumber(query['query_list'], testing=True)
    if not query_result: return 'No data'
    return render_template('query_results.html.j2', query_result=query_result, errors=errors)

@app.route('/process_file_query')
def process_file_query():
    
    return 'Hello there'

if __name__ == '__main__':
    app.run(debug=True)