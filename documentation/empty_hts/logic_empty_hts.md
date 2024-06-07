LEXICON:

- EH = Empty Htsno
- EHindent = Indent of the current EH
- EHfollowup = Empty Htsno following another empty htsno record

- queryState = Current level of query, example:
  - query = 0101.21.00.10
  - queryLevels = ["0101.21", "0101.21.00", "0101.21.00.10"]

USAGE:

**The algorithm will be used only if the current indent in the records has no coincidence with the current queryState (meaning that there is no additional descriptors present that can be used in the hts result creation)**

CASES:

1) EHindent == current queryState.indent && EHfollowup == False

    This means that there is an additional description for the hts, so we need to traverse from the EH index forward to check for a coincidence with the current queryState.

    We +1 the current queryState.index and run the checks again for coincidence with the queryState hts number, as well as this conditional in case there are two or more EH escalonated.

2) EHindent == current queryState.indent && EHfollowup == True

    This means that the previous EH can be used as part of the description for the final hts, alongside the current EH description, so we continue in this record index to check if the previous use case (1) is TRUE
    

        