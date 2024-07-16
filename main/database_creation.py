from scripts import update_hts_files, create_db
from utils import raw_hts_path, temp_hts_folder_path, string_folder_path, hts_folder_path

def run_database_creation():
    """Main database creation function, executes the workflows of hts temp files creation for both the HTS JSON files and the String_Dict, and the 

    """

    update_hts_files.writeFiles_workflow(
        update_hts_files.createHTSDict(raw_hts_path),
        temp_hts_folder_path, 
        string_folder_path, hts_folder_path)
    print(f'Temp files created at: {temp_hts_folder_path} - {string_folder_path} - {hts_folder_path}')

  
    create_db.create_database(hts_folder_path, string_folder_path)
    print('Databases created successfully')

    file_paths = [temp_hts_folder_path, string_folder_path, hts_folder_path]

    update_hts_files.deleteTempFiles(file_paths)

    print('Removed all files in the following folders:')

    for path in file_paths:
        print(path)
    

    
