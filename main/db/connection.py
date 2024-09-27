import pymongo
import db.credentialsDB as credentialsDB
from utils import util_functions

class Connection:
    """Class that connects to the database creating all necessary methods for connection and closing connection, as well as the base database for adding new HTS records and the string_dict collection too
    """

    def __init__(self, testing: bool):
        """_init_ function of the class, defines the connection variables

        Args:
            db_path (str): Path to the database connection on MongoDB
        """
        credentials = credentialsDB.loadEnvironmentVals()
        if testing:
            db_path = 'localhost'
            db_port = 27017
        else:
            option = input('You are using the production DB, enter Y to continue, N to cancel')
            if option == 'N':return
            db_path = f"{credentials['PATH_DB']}{credentials['USER_DB']}:{credentials['PW_DB']}@{credentials['CLUSTER_DB']}"
            db_port = None

        try:
            self.client = pymongo.MongoClient(host= db_path, port= db_port)
            self.db = self.client['hts']
            self.collection_records = self.db['hts_records']
            self.collection_string_dict = self.db['string_dict']
            if testing:
                print(f'Connected to {db_path} on {db_port}')
            else:
                print(f"Connected to: {credentials['PATH_DB']}, cluster: {credentials['CLUSTER_DB']}")
                print(f"User: {credentials['USER_DB']}")

        except Exception as exception:
            print('Error connecting to database')
            print(exception)
            raise

    def closeConnection(self):
        """Close connection function, closes current connection created in the Connection class
        """
        try:
            self.client.close()
            print('Closed connection to mongodb')
        except Exception as exception:
            print('Error closing connection')
            print(exception)
    
    def queryRecordsHTS(self, query_groups: list[dict[str, any]]) -> list[dict[str,any]]:
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
                    result.append({'data':'Missing record'})
                    print(f"Warning, no result found for {group['main_group']}")
                else: result.append(document)
            except Exception as exception:
                print(f"Failed query of record {group['main_group']}")
                print(exception)
        
        return result
    
    def queryStringDict(self, queryList: list[str]) -> dict[str,any]:
        """This function queries the string_dict collection in the DB and returns a list of results based on the query list provided of strings to query

        Args:
            queryList (list[str]): List of strings to pass to query

        Returns:
            list[dict[str,any]]: List of documents retrieved from the database
        """

        def grabChapterInfo(connection: Connection, document: dict[str,any]) -> dict[str,any]:
            """Function that queries the hts record collection and grabs the relevant record information for each of the chapters a string is present in the query

            Args:
                connection (Connection): Connection object from the database
                document (dict[str,any]): Document with the string_dict record information

            Returns:
                dict[str,any]: Returns a complete object with the chapter header information, the count of repeated times the string is present and the HTS record data
            """
            chapters = []

            for data in document['chaps']:
                chapter = connection.collection_records.find_one({'_id': data['chap']})
                chapters.append(util_functions.checkStringDescriptions(chapter, document['string'], data['count']))
            
            return chapters



        result = {}

        for query in queryList:
            try:
                document = self.collection_string_dict.find_one({'string': query})
                if document != None:
                    result[query] = grabChapterInfo(self, document)
                
            except Exception as exception:
                print(f'Failed to query string: {query}')
                print(exception)

        return result