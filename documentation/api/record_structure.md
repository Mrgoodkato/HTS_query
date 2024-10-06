### Record structures

#### Connection record:
{
    query:str,
    document: {
        id: ObjectId,
        header: str,
        data: list[dict[str, any]] 
    } OR str('Missing record')
}