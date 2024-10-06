# process_query
## query_hts_db.py - queryHTSNUmber(query:list)
### 1) createQueryGroups(query:list)
- returns query_groups: list[dict]: 
- {
- type:str, 
- main_group:str, 
- sub_groups:list[str]
- }
- uses functions in query_hts_input.py = processString() & processGroups()
### 2) Connection class instance creation
### 3) connection.queryRecordsHTS(query: list[dict]: 
###    {
###    type:str, 
###    main_group:str, 
###    sub_groups:list[str] })
###    returns:
- hts_documents list: dict[
- {
- id: ObjectId,
- header: str,
- data: list[dict] -> HTS record raw data
- } 
- OR { data: 'Missing record' }]
### 4) FOR EACH hts_documents element:
### query_hts_processing.py -> grabQueryRecords(hts_documents)
- parseQueryList() -> ERROR FOUND
