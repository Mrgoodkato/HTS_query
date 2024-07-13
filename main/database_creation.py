from scripts import update_hts_files
from utils import raw_hts_path, temp_hts_folder_path, string_folder_path, hts_folder_path

def run_database_creation():

    update_hts_files.writeFiles_workflow(
        update_hts_files.createHTSDict(raw_hts_path),
        temp_hts_folder_path, 
        string_folder_path, hts_folder_path)

