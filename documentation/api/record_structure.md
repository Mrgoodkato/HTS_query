### Record structures

#### Endpoints
1. `/process_query/`
   - This endpoint works by taking the `user_input` argument from the initial query form.
     
     EXAMPLE:
     - ```python
       user_input = '0101.02.02.01\n\r0101230211\n\r020302\n\r'
        #This input can be any kind of input from the user in the form of a string
   - This is passed as a raw string to the `processTextAreaInput()` which processes the raw string to produce a list of HTS codes based on if the user provided correctly formatted HTS as follows:
     - ```python
        processTextAreaInput = {
        'query_list': [<successful query strings>],
        'errors': [<unsuccesful query strings>]
        }
    - This result becomes the `query` object that is passed to the `queryHTSNumber()` pipeline that basically gathers all results from the DB and produces the final query result. As follows:
  
      - `query` is passed to the `createQueryGroups()` function which returns the query as follows:
      - ```python
        query_list = [
            {
                'type':str,    
                #This is the type of query, if Base_chapter, Base_semifull, etc, see note below.
                'main_group':str,  
                #First 4 characters of query to gather chapter in DB.
                'sub_groups':list[str],
                #List of subgroups that contain all the 6, 8 and 10 digit versions of the HTS code for querying the DB records.
                'full_query':str,
                #String result of the full query

            }, 
            {...},
        ]

        #type of records list from global_vars.py, list of tuples:
        
            (r'(^[\d]{4})([\d]{2})([\d]{2})([\d]{2})$', 'Statistical Suffix Record')
            (r'(^[\d]{4})([\d]{2})([\d]{2})$', 'Tariff Item Record')
            (r'(^[\d]{4})([\d]{2})$', 'Subheading Record') 
            (r'(^[\d]{4})$', 'Chapter Heading Record')
    - `Connection` instance is created to connect to DB and perform initial query.
    - `connection.queryRecordHTS()`is called with the `query_list` object. This function processes the list and returns the DB records gathered, as well as any errors in search:
      
      - ```python
        #When there is a result
        db_query_result = [
            {
            'query':dict[str,any], #The query object used with type, main_group and sub_groups
            'document': #Returned from DB if there is a result: 
              {
                  'id': ObjectId, #DB id
                  'header': str, #Header chapter number, e.g: 0101, 0102, 0103, etc...
                  'data': list[dict[str, any]] #HTS raw record
              }
            },
            #If there is no result:
            {
              'query':dict[str,any],
              'document':str #"Missing record"
            },
            {...},
        ] 
    
    - `Connection` instance is closed.
    - Iteration over the `db_query_result` list of records, each reacord goes through the `grabQueryRecords()`and from there into the `searchEHIndents()` functions to return the appropriate query info based on the query `sub_groups`. This information is saved in the `result` key added to the `db_query_result[index]` element of the list being iterated.
    - NOTE, there is a conditional that if the `document` key == to `Missing record`, it wont be processed this way.
      
      - ```python
        db_query_result[index] = {
            'query':dict[str,any],
            'document':{document object from DB},
            'result': list[dict[str,any]]
            #The result key is added with the final result of the query being sorted and organized in a list of dictionaries
        } 
    - Finally, this `result` list is iterated and pased into the `createDislayResult()` function, that translates the list of dictionaries into a new key called `display_resul of a simple dictionary for HTML and user display.
      - ```python
        db_query_result[index] = {
            'query':dict[str,any],
            'document':{document object from DB},
            'result': list[dict[str,any]]
            'display_result':dict[str,any]
            #Dictionary processed in simple strings for display to user.
        } 