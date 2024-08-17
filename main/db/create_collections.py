import pymongo, json, re
from db.connection import Connection

def createHTSDatabase(path_records: str, file_list: list, connection: Connection):
    """Main function to create the HTS database of records

    Args:
        path_records (str): Path to the .json divided record files
        file_list (list): List of filenames from the path_records for iteration
        connection (Connection): Connection class object that connects to the MongoDB instance
    """

    def addHTSRecord(folder_path: str, record: str, collection: pymongo.collection.Collection):
        """Specific function used by the createHTSDatabase() in order to add each document into the hts collection

        Args:
            folder_path (str): Path to folder where .json hts chapters are stored
            record (str): Name of file to be opened for addition
            collection (pymongo.collection.Collection): Pymongo collection object gathered from the Connection class
        """

        with open(f'{folder_path}{record}') as sec:


            data = json.load(sec)
            header = re.sub(r'\.json', '', record)

            hts_record = {
                'header': header,
                'data': data
            }

            try:
                collection.insert_one(hts_record)
            except:
                print(f'Error creating record in db for file {sec}')

    #Create Collection of records
    for file in file_list:
        print(f'Creating document {file} in hts_records collection...')
        addHTSRecord(path_records, file, connection.collection_records)

    print('Completed hts_records collection!')


def createStringDict(path_string_dict: str, connection: Connection):
    """Main function to create the string_dict collection in MongoDB

    Args:
        path_string_dict (str): Path to the json file with the string_dict information
        connection (Connection): Connection class object that connects to the MongoDB instance
    """

    def addStrRecord(str_chaps: list[dict[str,any]], key: str, connection: Connection):
        """Collects all the necessary information for the creation of each document in the string_dict collection

        Args:
            str_chaps (list[dict[str,any]]): Chapter list from the original string_dict json file that will be converted in its corresponding ObjectIds from the HTS collection in MongoDB
            key (str): Key word to be added to the collection representing the document
            connection (Connection): Connection class object that connects to the MongoDB instance
        """

        def queryHTSString(chaps: list[dict[str,any]], hts_collection: pymongo.collection.Collection):
            """Function helper of addStrRecord() that adds the ObjectId of each of the chapters in the list created in the string_dict json object.

            Args:
                chaps (list[dict[str,any]]): List of chapters to be queried in Mongo
                hts_collection (pymongo.collection.Collection): HTS collection already created and populated with chapter information for query

            Returns:
                list: Returns a list of ObjectIds from the hts collection from MongoDB to replace the string_dict list of chapters
            """

            ids = []

            for obj in chaps:

                #MongoDB returns a cursor iterator when we perform a find() query or aggregator as well, we need to also iterate it to gather the documents, or document
                cursor = hts_collection.find({ 'header': obj['chap'] })


                for document in cursor:
                    ids.append({
                        'chap': document['_id'],
                        'count': obj['count']
                                })
            
            return ids

        try:
            record = {
                'string': key,
                'chaps': queryHTSString(str_chaps, connection.collection_records)
            }
            connection.collection_string_dict.insert_one(record)
        except Exception as e:
            print(f'Error creating record in db for str_dict key: {key}, error: {e}')

    #Create Collection of string_dict
    with open(f'{path_string_dict}string_dict.json', 'r') as string_file:

        string_dict_raw = json.load(string_file)

        for key in string_dict_raw.keys():
            print(f'Creating document for <{key}> in string_dict collection...')
            addStrRecord(string_dict_raw[key], key, connection)
            
        print('Completed creating string_dict collection!')



      