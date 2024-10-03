from scripts.query_hts_input import *
from scripts.query_hts_processing import *
from db.connection import *
from utils.util_functions import createDisplayResult

def queryHTSNumber(input_query: list[str], testing: bool):

    query_result = []

    query_list = createQueryGroups(input_query)
    connection = Connection(testing)
    db_query_result = connection.queryRecordsHTS(query_list)
    connection.closeConnection()

    for index, result in enumerate(db_query_result):        
        final_result = []
        if result == 'No result':
            final_result.append('No result')
            continue
        grabbed_records = grabQueryRecords(result['data'], query_list[index])
        query_result.append(
            searchEHIndents(grabbed_records, result['data'])
        )

        for query in query_result:
            final_result.append(createDisplayResult(query))
    
    if not final_result: return None
    
    return final_result
    