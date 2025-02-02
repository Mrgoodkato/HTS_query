from scripts.query_hts_input import *
from scripts.query_hts_processing import *
from db.connection import *
from utils.util_functions import createDisplayResult, compareQueryWithResult
from logs import basic_logs as bl

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

    logger = bl.trace_logger('queryHTSNumberLogs.txt')
    separator = '\n\n-----------------------------------------------------------------------\n\n'
    if not db_query_result: return None

    for index, result in enumerate(db_query_result):

        if result['document'] == 'Missing record': continue

        logger.info(str(result) + separator + str(query_list[index]) + separator)        
        db_query_result[index]['pre-result'] = grabQueryRecords(result['document']['data'], query_list[index])
        logger.info('PRE-RESULT' + separator + str(db_query_result[index]['pre-result']) + separator)
        db_query_result[index]['result'] = searchEHIndents(db_query_result[index]['pre-result'], result['document']['data'])
        db_query_result[index]['display_result'] = createDisplayResult(db_query_result[index]['result'])
        db_query_result[index]['replaced_query'] = compareQueryWithResult(db_query_result[index]['query'], db_query_result[index]['display_result']['htsno'])
    
    return db_query_result
    