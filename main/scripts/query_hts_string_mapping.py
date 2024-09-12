from collections import defaultdict

def mapStringQuery(query_result: dict[list[dict[str,any]]]) -> dict[list[dict[str,any]]]:
    """Function that works by generating a map of the strings repeated in specific subchapters for better query occurrence handling.

    Args:
        query_result (dict[list[dict[str,any]]]): Initial query result of strings and their corresponding chapter information

    Returns:
        dict[list[dict[str,any]]]: Mapped result containing the information on each main chapter and the max occurrence of each string and string combinations found, as well as HTS number and index information for further query result structuring
    """

    chapter_classification = defaultdict(list)

    for query in query_result:

        for chap_item in query_result[query]:

            chapter_classification[chap_item['chap']].append({
                'query': query ,
                'count': chap_item['count'],
                'data': chap_item['data']
            })

        #This sorts by number of strings in the chapter
        sorted_map_str = dict(sorted(chapter_classification.items(), key=lambda item: len(item[1]), reverse=True))

        mapped_result_occurrence = {}
        #This sorts if two or more strings appear in the same indexHTS and creates a key of max_coincidence
        for chap in sorted_map_str:
            hts_sub_chap = {}
            for item in sorted_map_str[chap]:
                query_str = item['query']
                for data in item['data']:
                    if data['htsno'] == None:
                        key_EH = f"INDX-{data['indexHTS']}"
                        if key_EH in hts_sub_chap:
                            hts_sub_chap[key_EH]['ocurrence'] += 1
                            hts_sub_chap[key_EH]['query_str'].append(query_str)
                        else:
                            hts_sub_chap[key_EH] = {
                                'ocurrence': 1,
                                'htsdata':data,
                                'query_str': [query_str]
                            }
                    elif data['htsno'] in hts_sub_chap: 
                        hts_sub_chap[data['htsno']]['ocurrence'] += 1
                        hts_sub_chap[data['htsno']]['query_str'].append(query_str)
                    else: hts_sub_chap[data['htsno']] = {
                        'ocurrence': 1,
                        'htsdata':data,
                        'query_str': [query_str]
                    }
            
            mapped_result_occurrence[chap] = hts_sub_chap

    return mapped_result_occurrence

def sortMapByOccurrence(mapped_result_occurrence: dict[str,dict[str,any]]) -> dict[str,dict[str,any]]:
    """Function that sorts the mapped_result_ocurrence dictionary by both the number of ocurrences of queries, and then by the number of sub_chapters that were matched by the queries

    Args:
        mapped_result_occurrence (dict[str,dict[str,any]]): Mapped object with sorted_result information of sub_chapters, max_ocurrence and queries list

    Returns:
        dict[str,dict[str,any]]: Sorted object with order primarily by max_ocurrence and secondarily by sub_chapters
    """
    sorted_result = defaultdict(dict)
    for key, value in mapped_result_occurrence.items():

        ocurrence = 0
        queries = []
        for sub_key in value.keys(): 
            ocurrence  = ocurrence if ocurrence > value[sub_key]['ocurrence'] else value[sub_key]['ocurrence']
            queries.extend(value[sub_key]['query_str'])
            queries = list(set(queries))
        
        sorted_result[key]['data'] = dict(sorted(value.items(), key= lambda item: -item[1]['ocurrence']))
        sorted_result[key]['sorted_result'] = {
            'sub_chapters': len(value),
            'max_ocurrence': ocurrence,
            'queries': queries
        }
    
    sorted_result = dict(sorted(sorted_result.items(), key= lambda item: (-item[1]['sorted_result']['max_ocurrence'], -item[1]['sorted_result']['sub_chapters'])))

    return sorted_result