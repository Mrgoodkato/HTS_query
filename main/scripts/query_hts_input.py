import re
from utils.global_vars import punctuation_pattern, gather_hts_number

def processString(test_string: str) -> dict[str, any]:
    """Processes the string using the patterns for removing symbols and grouping the numbers according HTS syntax

    Args:
        test_string (str): Test string HTS number from user

    Returns:
        dict: Creates an object with 'type' of query and 'groups' Match object with the HTS grouped
    """

    string_no_symbols = re.sub(punctuation_pattern, '', test_string)

    for pattern in gather_hts_number:

        matched_str = re.match(pattern=pattern[0], string=string_no_symbols)

        if matched_str:
            return {
                'type': pattern[1],
                'groups': matched_str
            }
        
def processGroups(processed_str: dict) -> dict[str, any]:
    """Processes the groups from the originally processed string to add the HTS numbers for further database query

    Args:
        processed_str (dict): Object with the type and groups originally gathered from user input

    Returns:
        dict: Returns an object with 'type', 'main_group' and 'sub_groups' for DB query
    """
    def gatherGroups(groups: re.Match) -> list:
        """Helper method for the processGroups() that formats the HTS subrecords adding the previous numbers for database query

        Args:
            groups (re.Match): Match object containing each individual sub_record from user initial input

        Returns:
            list: Returns a list of hts sub_records for DB query
        """

        list_of_groups = []
        previous_group = ''
        first_run = True

        for i in range(1, len(groups.groups()) + 1):

            if first_run:
                previous_group = groups.group(i)
                first_run = False
            else:
                result = previous_group + '.' + groups.group(i)
                list_of_groups.append(result)
                previous_group = previous_group + '.' + groups.group(i)

        return list_of_groups

    query_chap = processed_str['groups'].group(1)
    groups = gatherGroups(processed_str['groups'])
    
    if len(groups) == 0:
        return {
            'type': processed_str['type'],
            'main_group': query_chap
        }
    else:
        return {
            'type': processed_str['type'],
            'main_group': query_chap,
            'sub_groups': groups
        }

def createQueryGroups(query_list: list) -> list[dict[str, any]]:
    """Main function that creates the query groups for DB query as a list of objects (for bulk query of several records)

    Args:
        query_list (list): List of strings or string in single element list containing raw input from user for hts query

    Returns:
        list: Returns a list of resulting objects\n \tThese objects are with type of query, main chapter, and sub_records if applicable for DB query, as follows \n
            'type': (str),
            'main_group': (str),
            'sub_groups': (list)
    """

    list_of_results = []

    for element in query_list:
        string_processed = processString(element)
        groups_processed = processGroups(string_processed)
        list_of_results.append(groups_processed)
        
    return list_of_results