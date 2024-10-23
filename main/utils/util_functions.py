import pandas as pd
import re
import json
from collections import Counter
from typing import List, Dict, Any
from utils.global_vars import key_words, punctuation_pattern, formatted_gather_hts_number

def removeEmptyKeysAndSave(htsdata: List[Dict[str, Any]], path: str):
    """This function removes the empty keys from the json chapter and saves it to the desired path

    Args:
        htsdata (List[Dict[str, Any]]): htsdata from a JSON file with the chapter info
        path (str): Path for saving the file
    """
    result = []

    for indx, data in enumerate(htsdata):
        
        filtered_data = {key: value for key, value in data.items() if value or value == 0}
        result.append(filtered_data)

    saveProcessedFile(result, path)

def saveProcessedFile(htsdata: List[Dict[str, Any]], path: str):
    """Saves the processed hts data info in the desired path

    Args:
        htsdata (List[Dict[str, Any]]): htsdata from a JSON file with the chapter info (used normally in the removeEmptyKeysAndSave() function)
        path (str): Path for saving
    """
    try:
        with open(path, 'w') as file:
            file.write(json.dumps(htsdata, indent=4))
            print(f'Saved final json {path}')
    except Exception as e:
        print(f'Could not save final file {path}')
        print(e)    

def addRowsToDataframe(df: pd.DataFrame, row: list):
    """Helper method used to easily add new rows to a pandas dataframe

    Args:
        df: pandas.DataFrame
            DataFrame to add the new rows to
        row (list): List to be added as a row into the dataframe
    """

    df.loc[len(df)] = row

def checkKeyWords(string: str) -> bool:
    """Checks against the keywords list for any matches in the string input

    Args:
        string (str): String that will be checked

    Returns:
        bool: True if the string does not coincide with the list, False if there is a match
    """

    for keyword in key_words:
        match = re.search(rf'^{keyword}$', string=string)
        if(match):
            return False
    
    return True

def openJSON(path: str) -> list[dict, any]:
    """Function that opens a JSON file and returns that file as a list

    Args:
        path (str): Path to the JSON file

    Returns:
        list: Returns a list object with the JSON information
    """

    with open(path, 'r') as file:
        result = json.loads(file.read())
    
    return result

def countStringOccurences(stringDict: dict[str,list[str]]) -> dict[str,list[dict[str, any]]]:
    """Function that takes the raw stringDict object and counts all occurrences of each of the chapters assigned to each string

    Args:
        stringDict (dict[list[str]]): Raw stringDict object with repeated chapter values

    Returns:
        dict[list[dict[str,any]]]: Returns a dict that lists each chapter where a string is located alongside how many times its repeated.
    """

    result = {}

    for key, values in stringDict.items():
        chapter_count = Counter(values)
        result[key] = [{'chap': chap, 'count': count} for chap, count in chapter_count.items()]

    return result

def checkStringDescriptions(hts_document: list[str,any], query_string: str, count: int) -> dict[str,any]:
    """Function that goes through the hts document gathered from the db and gets the relevant records with their index and hts number if present and returns them in a dictionary

    Args:
        hts_document (list[str,any]): Hts document gathered from DB
        query_string (str): String that will be searched against Hts document
        count (int): Count of occurrences of the string in the Hts document

    Returns:
        dict[str,any]: Resulting dictionary with chapter header, count and Hts document htsno's and indexes
    """

    result = {
        'chap': hts_document['header'],
        'count': count,
        'data': []
    }
    for key, doc in enumerate(hts_document['data']):
        
        description = re.sub(punctuation_pattern, '', doc['description'].lower())
        if re.search(query_string, description):
            
            result['data'].append({
                'htsno': doc.get('htsno', None),
                'indexHTS': key
            })
    
    return result

def createDisplayResult(raw_result: list[dict[str,any]])-> dict[str,any]:
    """This function takes the EH parsed HTS records and creates a dictionary for easier display in HTML and other formats

    Args:
        raw_result (list[dict[str,any]]): Original parsed query records, raw from EH final parsing

    Returns:
        dict[str,any]: Dictionary containing all key eleements to be displayed in other formats
    """
    
    display_result = {}

    for item in raw_result:

        for key, val in item.items():
            if val == None: continue
            if key == 'indent' or key == 'indexHTSRec' or key == 'missing': continue
            if key == 'units': 
                display_result[key] = ', '.join(val)
                continue
            if key == 'footnotes' and key not in display_result:
                display_result[key] = processFootnotes(val)
                continue

            if key not in display_result:
                display_result[key] = val
            elif key == 'htsno':
                display_result[key] = val
            elif isinstance(val, list) and key in display_result:
                display_result[key].extend(val)
            elif isinstance(val, str) and key in display_result:
                display_result[key] += ' ' + val
                
            
    return display_result

def processFootnotes(footnotes: list[dict[str,any]]) -> str:
    """Processes the footnotes of the HTS query result to gather the relevant information to display

    Args:
        footnotes (list[dict[str,any]]): Footnotes list object that contains additional information about the HTS result

    Returns:
        str: String containing the footnotes relevant information.
    """
    result = ''
    for note in footnotes:
        for key, val in note.items():
            if key == 'columns' or key == 'marker' or key == 'type': continue
            result += f'{val} '
    
    return result.strip()

def processTextAreaInput(raw_text: str)-> dict[str,list[str]]:
    """Function that takes the textarea input from the user, converts it to lists according to matches with HTS patterns, if they don't match, it adds to the error list, if it does, it adds to the result

    Args:
        raw_text (str): Raw textarea user input

    Returns:
        dict[str,list[str]]: Dictionary containing all the queries in list and all the errors in another list
    """
    hts_pattern = r'(?:^[\d]{4}\.[\d]{2}\.[\d]{2}\.[\d]{2}$|\\r)|(?:^[\d]{4}\.[\d]{2}\.(?:[\d]{2}|[\d]{4})$|\\r)|(?:^[\d]{4}\.(?:[\d]{2}|[\d]{4}|[\d]{6})$)|(?:^[\d]{4}$|\\r)|(?:^[\d]{6}$|\\r)|(?:^[\d]{8}$|\\r)|(?:^[\d]{10}$|\\r)'
    raw_list = raw_text.splitlines()
    print(f'processTextAreaInput - raw list:{raw_list}')
    final_list = {
        'query_list': [],
        'errors': []
    }
    for string in raw_list:
        
        if re.match(hts_pattern, string):
            final_list['query_list'].append(string)
        else:
            final_list['errors'].append(string)

    print(f'processTextAreaInput - final list:{final_list}')
    return final_list

def compareQueryWithResult(query: dict[str,any], result: str) -> dict[str,any]:
    """This function adds more information to the resulting query by comparing with the actual final queried result against the initial query and returning the corresponding information

    Args:
        query (dict[str,any]): Original query list composed of the type, main group, sub groups and full query
        result (str): Resulting query after being retrieved from DB

    Returns:
        dict[str,any]: Dictionary with values for further display in the results page in order to convert or offer additional info if there are discrepancies.
    """
    
    for item in formatted_gather_hts_number:

        if re.match(item[0], result) and item[1] != query['type']: return {
            'replace_to': item[1],
            'original_query': query['full_query'],
            'result_query': result,
            'missing_numbers': re.sub(result, '', query['full_query'])
        }
    
    return {
        'replace_to': None
    }