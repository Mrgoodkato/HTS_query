from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

PATH_DB = os.getenv('PATH_DB')
USER_DB = os.getenv('USER_DB')
PW_DB = os.getenv('PW_DB')
CLUSTER_DB = os.getenv('CLUSTER_DB')