def searchEHIndents(result_query: list[dict[str, any]], hts_record: list[dict[str, any]]) -> list[dict[str, any]]:
    """Function that search for the Empty HTS records in the current result_query and adds their information to the final result

    Args:
        result_query (list[dict[str, any]]): Result of the original query to the hts_record with all valid matches for the original query string
        hts_record (list[dict[str, any]]): Main record where all the query information is located

    Returns:
        list[dict[str, any]]: Returns a list of dictinaries with the result_query and the EH records (if present).
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

    for key, result in enumerate(result_query):

        result_final.append(result)

        if 'missing' not in result: continue

        indents = result_query[key]['missing']
        eh_records = createEHRecords(indents)

        for i in range(result['indexHTSRec'], result_query[key+1]['indexHTSRec']):

            for rec in eh_records:

                if 'htsno' not in hts_record[i] and rec['indent'] == hts_record[i]['indent']:
                    
                    rec['description'] = hts_record[i]['description']
        
        
        if eh_records: result_final.extend(eh_records)

    return result_final