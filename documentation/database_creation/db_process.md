# database_creation.py
## run_database_creation()
### update_hts_file.py
- writeFiles_workflow()
    - **(params)**
      - createHTSDict()
        - Downloads HTS json from customs and cretes the HTS dictionary object with all HTS info
        - **(params)**
          - path
            - Path to the raw HTS download folder
      - path_hts
        - Path to the JSON HTS individual files folder (raw parse)
      - path_strings
        - Path to the string_dict folder
      - path_final
        - Path to the JSON HTS individual files folder (parsed for empty records)
### create_db.py
- create_database()