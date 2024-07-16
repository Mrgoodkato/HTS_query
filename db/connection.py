import pymongo
import db.credentialsDB as credentialsDB

class Connection:
    """Class that connects to the database creating all necessary methods for connection and closing connection, as well as the base database for adding new HTS records and the string_dict collection too
    """

    def __init__(self):
        """_init_ function of the class, defines the connection variables

        Args:
            db_path (str): Path to the database connection on MongoDB
        """

        db_path = f'{credentialsDB.PATH_DB}{credentialsDB.USER_DB}:{credentialsDB.PW_DB}@{credentialsDB.CLUSTER_DB}'

        try:
            self.client = pymongo.MongoClient(db_path)
            self.db = self.client['hts']
            self.collection_records = self.db['hts_records']
            self.collection_string_dict = self.db['string_dict']
            print(f'Connected to: {credentialsDB.PATH_DB}, cluster: {credentialsDB.CLUSTER_DB}')
            print(f'User: {credentialsDB.USER_DB}')

        except Exception as exception:
            print('Error connecting to database')
            print(exception)

    def closeConnection(self):
        """Close connection function, closes current connection created in the Connection class
        """
        try:
            self.client.close()
        except Exception as exception:
            print('Error closing connection')
            print(exception)