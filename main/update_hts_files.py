import pandas as pd
import re
import json
from typing import List, Dict, Any
from utils import *

def createHTSDict(path: str) -> dict[pd.DataFrame, any]:
    """Method that creates a dictionary object with all the HTS data from the CBP site in JSON format for all chapters.

    Args:
        path (str): Path of the original HTS JSON file downloaded from CBP

    Returns:
        dict: Dictionary object with all the information in the original HTS file
    """

    df = pd.read_json(path)
    columns_df = df.columns.tolist()
    final_dict = {}
    main_numbers_pattern = re.compile(r'^[\d]{4}')
    start = True
    current_main_hts = ['']
    previous_main_hts = ['']
    total_rows = countDFLength(df.iterrows())
    current_row = total_rows

    for index, row in df.iterrows():

        current_main_hts = main_numbers_pattern.findall(row['htsno'])

        if start:
            previous_main_hts = current_main_hts
            final_dict[current_main_hts[0]] = pd.DataFrame(columns=columns_df)
            addRowsToDataframe(final_dict[current_main_hts[0]], row)

        if len(current_main_hts) == 0:
            current_main_hts = previous_main_hts

        if (previous_main_hts[0] != current_main_hts[0]) and (len(current_main_hts)):
            final_dict[current_main_hts[0]] = pd.DataFrame(columns=columns_df)
            addRowsToDataframe(final_dict[current_main_hts[0]], row)
            previous_main_hts = current_main_hts  
        elif start == False:
            addRowsToDataframe(final_dict[current_main_hts[0]], row)
        start = False

        current_row -= 1
        print(f'Progress creating dictionary {HTSDictProgressCount(current_row, total_rows)}', end='\r')

    return final_dict

def writeFiles_workflow(HTS_dict: dict[pd.DataFrame, any], path_hts: str, path_strings: str, path_final: str):
    """Writes all header sections of HTS codes into individual JSON files with the header number as filename. And creates a single JSON file containing all keywords with lists of the HTS file names where they are located

    Args:
        HTS_dict (dict): HTS dictionary object with all the chapter information from CBP
        path_hts (str): Path to store the individual HTS JSON files divided by header code
        path_strings (str): Path to store the string dictionary into a JSON file
        path_final (str): Path for the final JSON files with no empty keys
    """

    string_dict = {}
    file_dict = {}
    file_path = 'string_dict.json'

    for key,df in HTS_dict.items():
        
        file_dict[key] = f'{path_hts}/{key}.json'

        try:
            df.to_json(file_dict[key], orient='records')
            print(f'File {key}.json - written')

            with open(file_dict[key], 'r') as jsonfile:
                removeEmptyKeysAndSave(json.loads(jsonfile.read()), f'{path_final}/{key}.json')    
            
        except Exception as e:
            print(f'Error writing file {key}.json')
            print(e)

        for row in df.iterrows():
            desc = re.sub(pattern=punctuation_pattern, repl='', string=row[1]['description']).lower()
            
            array_string = desc.split()
            
            if(len(array_string) <= 0): continue
            
            for string in array_string:
                if(checkKeyWords(string) == False): continue

                if(string in string_dict):
                    string_dict[string].append(key)
                    string_dict[string] = list(set(string_dict[string]))
                    print(f'string_dict key "{string}" added chapter "{key}"')
                    continue
            
                string_dict[string] = []
                string_dict[string].append(key)
                string_dict[string] = list(set(string_dict[string]))
                print(f'string_dict added string "{string}" with chapter "{key}"')

    with open(f'{path_strings}{file_path}', 'w') as json_file:
        json.dump(string_dict, json_file, indent=4)