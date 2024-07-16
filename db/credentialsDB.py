from dotenv import load_dotenv
import os

load_dotenv()

PATH_DB = os.getenv('PATH_DB')
USER_DB = os.getenv('USER_DB')
PW_DB = os.getenv('PW_DB')
CLUSTER_DB = os.getenv('CLUSER_DB')