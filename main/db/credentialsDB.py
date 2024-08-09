from dotenv import load_dotenv
import os

def loadEnvironmentVals():

    env_path = os.path.join(os.path.dirname(__file__), '.env')
    print(env_path)
    load_dotenv(dotenv_path=env_path)

    return {
        'PATH_DB': os.getenv('PATH_DB'),
        'USER_DB': os.getenv('USER_DB'),
        'PW_DB': os.getenv('PW_DB'),
        'CLUSTER_DB': os.getenv('CLUSTER_DB')
    }
    