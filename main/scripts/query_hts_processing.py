import re

def grabQueryRecords(hts_record: list[dict[str, any]], query: dict[str, any]) -> list[dict[str, any]]:
    """Function that iterates the original HTS full record and parses against the coincidences found in the query list (query list containing the main and sub query numbers entered at the time of query)

    Args:
        hts_record (list[dict[str, any]]): Full HTS record grabbed from db
        query [dict[str, any]): Dict of query numbers in the original query input

    Returns:
        list[dict[str, any]]: HTS parsed record of coincidences matching the query list elements against original HTS record
    """

    def parseQueryList(query: dict[str, any]) -> list[str]:
        """Helper function that works by grabbing the 'main_group' and 'sub_groups' items in the original query and joining them in a single str list

        Args:
            query (dict[str, any]): Original query object with 'main_group' and with or without 'sub_groups'

        Returns:
            list[str]: Resulting str list of all htsno records to be queried
        """
        
        queryList = [query['main_group']]
        if 'sub_groups' in query:
            queryList.extend(query['sub_groups'])

        return queryList


    def checkResultQuery(result_query: list[dict[str, any]]):
        """Helper function that takes the original query records grabbed and tags the missing indents after parsing, adding the 'missing' tag to each with missing indents for further processing

        Args:
            result_query (list[dict[str, any]]): Result of the original grabQueryRecords() logic that has all parsed coincidences with original HTS record
        """

        index = 0
        indent_list = [record['indent'] for record in result_query if 'indent' in record]

        for i in range(0, result_query[-1]['indent']):
            
            if i not in indent_list:
        
                if 'missing' in result_query[index-1]:

                    result_query[index-1]['missing'].append(i)
                else:
                    result_query[index-1]['missing'] = [i]

            else:
                index += 1


    result = []
    index_query = 0
    queryList = parseQueryList(query)
    print(queryList)

    while index_query < len(queryList):

        for key, record in enumerate(hts_record):
            
            if 'htsno' in record and re.match(rf'{queryList[index_query]}$', record['htsno']):
                obj = record
                result.append(obj.update({}))

        index_query += 1
    
    checkResultQuery(result)
    
    return result

def searchEHIndents(result_query: list[dict[str, any]], hts_records: list[dict[str, any]]) -> list[dict[str, any]]:
    """Function that search for the Empty HTS records in the current result_query and adds their information to the final result

    Args:
        result_query (list[dict[str,any]]): Result of the original query to the hts_records with all valid matches for the original query string
        hts_records (list[dict[str,any]]): Main record where all the query information is located

    Returns:
        list[dict[str,any]]: Returns a list of dictinaries with the result_query and the EH records (if present).
    """
    
    def createEHRecords(indents: list[int]) -> list[dict[str, int]]:
        """Helper function that creates the main EH record object list with just the indent key and value

        Args:
            indents (list[int]): Original indent list grabbed from the result_query object

        Returns:
            list[dict[str, int]]: Final object list with the indents as key-value pairs.
        """

        result = []
        
        for indent in indents:

            result.append({
                'indent': indent
            })
        
        return result
    
    result_final = []

    for indx, result in enumerate(result_query):

        result_final.append(result)

        if 'missing' not in result: continue
        if len(result) == 0: continue

        indents = result_query[indx]['missing']
        eh_records = createEHRecords(indents)

        for i in range(result['indexHTSRec'], result_query[indx+1]['indexHTSRec']):

            for rec in eh_records:

                if 'htsno' not in hts_records[i] and rec['indent'] == hts_records[i]['indent']:
                    
                    rec['description'] = hts_records[i]['description']
        
        
        if eh_records: result_final.extend(eh_records)

    return result_final