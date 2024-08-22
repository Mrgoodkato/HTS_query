from scripts import update_hts_files, create_db
from utils.global_vars import raw_hts_path, temp_hts_folder_path, string_folder_path, hts_folder_path

def run_database_creation(testing: bool):
    """Main database creation function, executes the workflows of hts temp files creation for both the HTS JSON files and the String_Dict, and the 

    Args:
        testing (bool): Defines if testing, local DB will be used (needs mongo installed in system)
    """

    option = input('Starting the process of HTS and String Dict creation, run?\nY/N')

    if(option.upper() == 'Y'):
        update_hts_files.writeFiles_workflow(
            update_hts_files.createHTSDict(raw_hts_path),
            temp_hts_folder_path, 
            string_folder_path, hts_folder_path)
        print(f'Temp files created at: {temp_hts_folder_path} - {string_folder_path} - {hts_folder_path}')
    else:
        print('Process cancelled')
        return
    
    option = input("Create database collections for HTS and String Dict?\nBe advised this process might take from 4-6 hours to complete\nY/N")

    if(option.upper() == 'Y'):

        create_db.create_database(hts_folder_path, string_folder_path, testing)
        print('Databases created successfully')
    
    option = input('Delete the created JSON files for HTS and String Dict?')
    
    file_paths = [temp_hts_folder_path, string_folder_path, hts_folder_path]
    
    if(option.upper() == 'Y'):

        update_hts_files.deleteTempFiles(file_paths)

        print('Removed all files in the following folders:')

        for path in file_paths:
            print(path)
        
        return
    else:
        print(f'Files remain at the following folders:\n{temp_hts_folder_path}\n{string_folder_path}\n{hts_folder_path}')

    
