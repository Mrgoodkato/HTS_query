import logging
import os
import json

#UTIL FUNCTIONS
def remove_old_log(folder_path:str, file_name:str):
    """Function to remove the old log from the system

    Args:
        folder_path (str): Folder path, normally logs/trace_logger/
        file_name (str): Name of the logger file
    """
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            print(f'Removed old log from {file_path}')
            return
        except Exception as e:
            print(f'Error deleting file {file_path}')
            return
    return

#LOGGER FUNCTIONS
def basic_logger(data: list[dict,any], filename: str, mode: str):
    """Method to log different txt results to the folder 'logs/txt_logs/' or 'logs/json_logs/'

    Args:
        data (list[dict,any]): Data to log
        filename (str): Filename to be used
        mode (str): Either 'txt' or 'json' defines the folder to be used
    """
    json_folder = 'logs/json_logs/'
    txt_folder = 'logs/txt_logs/'
    
    if mode == 'txt':
        with open(f'{txt_folder}{filename}.txt', 'w', encoding="utf-8") as log_file: log_file.write(str(data))
    else:
        with open(f'{json_folder}{filename}.json', 'w') as log_file:
            json.dump(data, log_file, indent=1)



def trace_logger(file_name:str) -> logging.Logger:
    """Trace logger creator, this creaates a logger that appends detailed information about a process into a txt file

    Args:
        file_name (str): filename to be used in the logs folder called trace_logger

    Returns:
        logging.Logger: Returns a logger object that can be used to append logging information into a txt file
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))  
    project_root = os.path.abspath(os.path.join(root_dir, "../logs/trace_logger"))  
    
    # Create the full path for the log file
    log_file_path = os.path.join(project_root, file_name)

    # Ensure the directory for the log file exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    remove_old_log(project_root, file_name)

    logger = logging.getLogger("fileLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        flie_handler = logging.FileHandler(log_file_path, mode="a")
        flie_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        flie_handler.setFormatter(formatter)
        logger.addHandler(flie_handler)
    
    return logger