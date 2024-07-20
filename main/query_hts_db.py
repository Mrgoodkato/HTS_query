from scripts.query_hts_input import *
from scripts.query_hts_processing import *
from db.connection import Connection

def queryHTSMulti(input_query: list[str]):

    query_list = createQueryGroups(input_query)

    connection = Connection()

    db_query_result = connection.queryRecordsHTS(query_list, connection)
    
    return searchEHIndents(query_list, db_query_result)
    