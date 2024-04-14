import pandas as pd
import re
import json
import os
from global_vars import addRowsToDataframe, checkKeyWords, openJSON, processRecord, punctuation_pattern

def createHTSDict(path: str):
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

    for index,row in df.iterrows():

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

    return final_dict

def writeFiles(HTS_dict: dict, path_hts: str, path_strings: str):
    """Writes all header sections of HTS codes into a single JSON file into a path_hts folder. And creates a single JSON file containing all keywords with lists of the HTS file names where they are located

    Args:
        HTS_dict (dict): HTS dictionary object with all the chapter information from CBP
        path_hts (str): Path to store the individual HTS JSON files divided by header code
        path_strings (str): Path to store the string dictionary into a JSON file
    """

    string_dict = {}
    file_dict = {}

    for key,df in HTS_dict.items():
        
        file_dict[key] = f'{path_hts}/{key}.json'

        df.to_json(file_dict[key], orient='records')

        for row in df.iterrows():
            desc = re.sub(pattern=punctuation_pattern, repl='', string=row[1]['description']).lower()
            
            array_string = desc.split()
            if(len(array_string) > 0):
                for string in array_string:
                    if(string in string_dict): 
                        string_dict[string].append(key)
                        string_dict[string] = list(set(string_dict[string]))
                    else:
                        if(checkKeyWords(string)): 
                            string_dict[string] = []
                            string_dict[string].append(key)
                            string_dict[string] = list(set(string_dict[string]))
                            
        file_path = 'string_dict.json'

        with open(f'{path_strings}{file_path}', 'w') as json_file:
            json.dump(string_dict, json_file, indent=4)

def removeEmptyHTS(folder: str):
    """Method that overwrites the already created json HTS files, processing them again so they are passed on without the empty "htsno" sections.

    Args:
        folder (str): Folder where the already processed json files are located
    """

    filenames = os.listdir(folder)

    for file in filenames:

        record = openJSON(f'{folder}{file}')
        processed_record = processRecord(record)

        with open(f'{folder}{file}', 'w') as final_file:
            json.dump(processed_record, final_file, indent=4)