def basic_logger(data: list[dict,any], filename: str):
    """Method to log different txt results to the folder 'logs/txt_logs/'

    Args:
        data (list[dict,any]): Data to log
        filename (str): Filename to be used
    """
    with open(f'logs/txt_logs/{filename}.txt', 'w', encoding="utf-8") as log_file: log_file.write(str(data))
