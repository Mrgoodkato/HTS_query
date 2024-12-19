def basic_logger(data): 
    with open('logs/txt_logs/basic_logs.txt', 'a') as log_file: log_file.write(str(data))
