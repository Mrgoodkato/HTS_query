import os
from dotenv import credentials
from db import Connection, create_collections
from utils import hts_folder_path, string_folder_path

def create_database():

    file_list = os.listdir(hts_folder_path)

    connection = Connection(f'{credentials.PATH_DB}{credentials.USER_DB}:{credentials.PW_DB}@{credentials.CLUSTER_DB}')

    create_collections.createHTSDatabase(hts_folder_path, file_list, connection)
    create_collections.createStringDict(string_folder_path, connection)
