from scripts.query_hts_input import *
from db.connection import Connection

def queryHTS(input_query: list[str]):

    processed_query_list = createQueryGroups(input_query)

    connection = Connection()

    db_query_result = connection.queryRecordsHTS(processed_query_list, connection)

    for query in processed_query_list:

        