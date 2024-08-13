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
        credentials = credentialsDB.loadEnvironmentVals()
        db_path = f"{credentials['PATH_DB']}{credentials['USER_DB']}:{credentials['PW_DB']}@{credentials['CLUSTER_DB']}"
        print(db_path)

        try:
            self.client = pymongo.MongoClient(db_path)
            self.db = self.client['hts']
            self.collection_records = self.db['hts_records']
            self.collection_string_dict = self.db['string_dict']
            print(f"Connected to: {credentials['PATH_DB']}, cluster: {credentials['CLUSTER_DB']}")
            print(f"User: {credentials['USER_DB']}")

        except Exception as exception:
            print('Error connecting to database')
            print(exception)

    def closeConnection(self):
        """Close connection function, closes current connection created in the Connection class
        """
        try:
            self.client.close()
            print('Closed connection to mongodb')
        except Exception as exception:
            print('Error closing connection')
            print(exception)
    
    def queryRecordsHTS(self, query_groups: list[dict[str, any]]) -> list[dict[str, any]]:
        """This function queries the hts_records collection to retrieve the full records for a given list of queries (hts numbers)

        Args:
            query_groups (list[dict[str, any]]): Query hts groups organized for database query.

        Returns:
            list[dict[str,any]]: Resulting records from DB in list.
        """

        result = []

        for group in query_groups:

            try:
                document = self.collection_records.find_one(
                    {'header': group['main_group']}
                )
                if document == None: 
                    result.append('No result')
                    print(f"Warning, no result found for {group['main_group']}")
                else: result.append(document)
            except Exception as exception:
                print(f"Failed query of record {group['main_group']}")
                print(exception)
        
        return result