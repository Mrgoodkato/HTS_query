import os
from db.connection import Connection
from db import create_collections

def create_database(hts_folder_path: str, string_folder_path: str):
    """Function that handles the creation of the database using the temporary JSON files created previously in the temp folder

    Args:
        hts_folder_path (str): Folder path for the JSON hts files in the temp folder
        string_folder_path (str): Folder path for the string_dict JSON file in the temp folder
    """

    hts_file_list = os.listdir(hts_folder_path)

    connection = Connection()

    create_collections.createHTSDatabase(hts_folder_path, hts_file_list, connection)
    create_collections.createStringDict(string_folder_path, connection)

    connection.closeConnection()
