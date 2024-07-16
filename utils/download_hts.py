import requests
import os
import json
from utils.global_vars import raw_hts_dir_path

def run_download_hts() -> bool:

    url = 'https://hts.usitc.gov/reststop/exportList?from=0101&to=9999.&format=JSON&styles=true'

    response = requests.get(url)

    if response.status_code == 200:

        json_data = response.json()

        if not os.path.exists(raw_hts_dir_path):
            os.makedirs(raw_hts_dir_path)

        file_path = os.path.join(raw_hts_dir_path, 'htsdata.json')

        with open(file_path, 'w') as file:
            json.dump(json_data, file)
        
        print(f'Successfully saved file into {file_path}')
        return True
    
    else:
        print(f'Unable to download file to {file_path}')
        print(f'Download performed from {url}')
        return False
