import pandas as pd
import re
import json
from global_vars import key_words


def addRowsToDataframe(df: pd.DataFrame, row: list):
    """Helper method used to easily add new rows to a pandas dataframe

    Args:
        df: pandas.DataFrame
            DataFrame to add the new rows to
        row (list): List to be added as a row into the dataframe
    """

    df.loc[len(df)] = row

def checkKeyWords(string: str):
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

def openJSON(path: str):
    """Function that opens a JSON file and returns that file as a list

    Args:
        path (str): Path to the JSON file

    Returns:
        list: Returns a list object with the JSON information
    """

    with open(path, 'r') as file:
        result = json.loads(file.read())
    
    return result

def processRecord(record: list):
    """Helper method that works by iterating each JSON HTS record already processed, and eliminates the empty htsno records, adding their description to the next sections following the indent logic

    Args:
        record (list): JSON processed list containing several sections to be iterated
    
    Returns:
        list: Returns the resulting sections in a list without the empty htsno sections and correctly appeding the descriptions of empty htsno sections to their corresponding sections. 
    """

    result = []
    saved_section_description = {
        'description': '',
        'indent': 0,
        'current': False
    }

    for section in record:

        if section['htsno'] == '':

            saved_section_description = {
                'description': section['description'],
                'indent': section['indent'],
                'current': True
            }
            continue
        
        if saved_section_description['current'] == True:

            if saved_section_description['indent'] == (section['indent'] -1):
                section['description'] += f' | {saved_section_description['description']}'
            
            else:
                saved_section_description['current'] = False

        result.append(section)
    
    return result