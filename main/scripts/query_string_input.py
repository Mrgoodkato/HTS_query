import re
from utils.global_vars import punctuation_pattern
from utils.util_functions import checkKeyWords

def processInitialString(queryRaw: str):
    """Function that takes the initial string query and parses it to a list with removed punctuation signs and common words

    Args:
        queryRaw (str): Initial query input string

    Returns:
        _type_: List of strings from initial query parsed
    """

    query_list = queryRaw.lower().split(' ')
    query_list_processed = []

    for query in query_list:

        query_processed = re.sub(punctuation_pattern, '', query)
        if checkKeyWords(query_processed): query_list_processed.append(query_processed)

    return query_list_processed