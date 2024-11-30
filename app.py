import sys, os
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

    try:
        data = request.get_json()
        user_input = data.get('user_input') if data else None
        if not user_input:
            return jsonify({"message": "No input provided"}), 400
        processed_data = user_input
        query = processTextAreaInput(processed_data)
        errors = query['errors']
        query_result = query_hts_db.queryHTSNumber(query['query_list'], testing=True)
        if not query_result: return 'No data'
        return render_template('query_results.html.j2', query_result=query_result, errors=errors)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
   
@app.route('/process_file_query')
def process_file_query():
    
    return 'Hello there'

if __name__ == '__main__':
    app.run(debug=True)