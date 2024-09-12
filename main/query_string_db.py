from db import connection
from scripts import query_string_input, query_hts_string_mapping

def queryStringDb(query_str: str, testing: bool) -> dict[str, dict[str,any]]:

    query_list = query_string_input.processInitialString(query_str)
    conn = connection.Connection(testing)
    query_result = conn.queryStringDict(query_list)
    conn.closeConnection()
    mapped_result = query_hts_string_mapping.mapStringQuery(query_result)
    sorted_result = query_hts_string_mapping.sortMapByOccurrence(mapped_result)

    return sorted_result
