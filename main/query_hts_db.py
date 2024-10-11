from scripts.query_hts_input import *
from scripts.query_hts_processing import *
from db.connection import *
from utils.util_functions import createDisplayResult

def queryHTSNumber(input_query: list[str], testing: bool)-> list[dict[str,any]]:
    """Function that receives an input query string list and queries against the HTS database, getting and parsing the results

    Args:
        input_query (list[str]): List of query HTS numbers to be searched
        testing (bool): True if using testing Mongo DB database, or False if using production DB server

    Returns:
        list[dict[str,any]]: Returns a query/document object as follows:
        [
            {
                query:list[dict[str,any]] -> #query groups,
                document:dict[str,any] #OR str('Missing record'),
                result:list[dict[str,any]] -> #resulting records queried, raw response
                display_result: dict[str,any] -> #resulting records parsed for display in HTML or other formats
            }
        ]
    """
    query_list = createQueryGroups(input_query)
    connection = Connection(testing)
    db_query_result = connection.queryRecordsHTS(query_list)
    connection.closeConnection()

    if not db_query_result: return None

    for index, result in enumerate(db_query_result):

        if result['document'] == 'Missing record': continue

        db_query_result[index]['result'] = searchEHIndents(grabQueryRecords(result['document'], query_list[index]), result['document'])
        print(db_query_result[index]['result'])
        db_query_result[index]['display_result'] = createDisplayResult(db_query_result[index]['result'])
        print(db_query_result[index]['display_result'])

    
    return db_query_result
    