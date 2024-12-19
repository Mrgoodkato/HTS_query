import pandas as pd

def saveExcelDF(data_query: list[dict, any]):

    data = []

    for query in data_query:
        data.append({key: value for key, value in query['display_result'].items()})

    df = pd.DataFrame(data)
    df.to_excel('logs/xlsx_logs/query_excel.xlsx')
