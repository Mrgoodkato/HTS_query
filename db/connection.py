import pymongo

class Connection:
    """Class that connects to the database creating all necessary methods for connection and closing connection, as well as the base database for adding new HTS records and the string_dict collection too
    """

    def __init__(self, db_path: str):
        """_init_ function of the class, defines the connection variables

        Args:
            db_path (str): Path to the database connection on MongoDB
        """

        self.client = pymongo.MongoClient(db_path)
        self.db = self.client['hts']
        self.collection_records = self.db['hts_records']
        self.collection_string_dict = self.db['string_dict']
        

    def closeConnection(self):
        """Close connection function, closes current connection created in the Connection class
        """
        self.client.close()