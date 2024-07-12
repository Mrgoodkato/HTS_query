from update_hts_files import *
from utils import raw_hts_path, temp_hts_folder_path, string_folder_path, hts_folder_path

def write_files():

    writeFiles_workflow(createHTSDict(raw_hts_path),temp_hts_folder_path, string_folder_path, hts_folder_path)
