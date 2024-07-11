def countDFLength(iterrows: list) -> int:
    """Counts the number of rows in the original htsdata.json file df

    Args:
        iterrows (list): List of rows from iterator for counting

    Returns:
        int: Number of rows of htsdata.json df
    """
    count = 0
    for row in iterrows:
        count += 1
    
    return count

def HTSDictProgressCount(current: int, total: int) -> int:

    return f'{int((current/total) * 100)}%'