import pandas as pd
import re
import json
from typing import List, Dict, Any
from global_vars import key_words

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