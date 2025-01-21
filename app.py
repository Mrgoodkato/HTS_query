import sys, os
from logs import basic_logs as bl
from openpyxl import Workbook, load_workbook
from flask import Flask, render_template, request, session, jsonify, send_file, url_for, redirect
sys.path.append(os.path.abspath('main'))
from main import query_hts_db, query_string_db
from main.utils.util_functions import processTextAreaInput
from main.utils.process_excel import saveExcelDF

app = Flask(__name__)
app.secret_key = 'my_keyDEVELOPMENTONLY'

@app.route('/')
def index():
    return render_template('home.html.j2', title='Enter query')

@app.route('/process_query', methods=['POST'])
def process_query():
    session.permanent = False
    session.clear()
    user_input = request.form.getlist('user_input') or request.form.getlist('user_input_manual')
    bl.basic_logger(str(request.form), 'request_process_query')
    query_string = '\n'.join(user_input)
    query = processTextAreaInput(query_string)
    errors = query['errors']
    query_result = query_hts_db.queryHTSNumber(query['query_list'], testing=True)
    session['query_results'] = query_result
    session['query_errors'] = errors
    bl.basic_logger(str(session.items()), 'session')

    if not query_result: return 'No data'
    return render_template('query_results.html.j2', query_result=query_result, errors=errors)

@app.route('/process_file_query')
def process_file_query():
    
    return 'Hello there'

@app.route('/download_query')
def download_query():
    
    data_query = session.get('query_results')
    data_errors = session.get('query_errors')
    bl.basic_logger(data_query, 'data_query')
    saveExcelDF(data_query)
    
    return 'Success!'

if __name__ == '__main__':
    app.run(debug=True)