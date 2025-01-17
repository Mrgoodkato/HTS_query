key_words = ['a', 'able', 'about', 'above', 'across', 'actually', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', "aren't", 'as', 'aside', 'at', 'available', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'being', 'below', 'beside', 'besides', 'between', 'both', 'but', 'by', "can't", 'cannot', 'certain', 'certainly', 'clearly', 'co', 'com', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', 'currently', 'definitely', 'described', 'despite', 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'downwards', 'during', 'each', 'else', 'elsewhere', 'enough', 'especially', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'far', 'few', 'following', 'for', 'former', 'formerly', 'forth', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', "how's", 'howbeit', 'i', "i'd", "i'll", "i'm", "i've", 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'indicate', 'indicated', 'indicates', 'inner', 'insofar', 'instead', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'latter', 'latterly', 'least', 'lest', "let's", 'like', 'liked', 'likely', 'likewise', 'look', 'looking', 'looks', 'ltd', 'may', 'maybe', 'me', 'meanwhile', 'merely', 'might', 'more', 'moreover', 'most', 'mostly', 'much', 'must', "mustn't", 'my', 'myself', "n't", 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'next', 'no', 'non', 'none', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular', 'particularly', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'several', 'shall', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', "t's", 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that's", 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', "there's", 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'think', 'third', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'un', 'under', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'value', 'various', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", "we'll", "we're", "we've", 'welcome', 'well', 'went', 'were', "weren't", 'what', "what's", 'whatever', 'when', "when's", 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', "who's", 'whoever', 'whole', 'whom', 'whose', 'why', "why's", 'will', 'willing', 'wish', 'with', "won't", 'wonder', 'would', "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

punctuation_pattern = r'[!\"#$%&\'()*+,-./:;<=>?@\[\]\^_`{|}~—]'

gather_hts_number = [
    (
        r'(^[\d]{4})([\d]{2})([\d]{2})([\d]{2})$', 'Statistical Suffix Record'
    ),
    (
        r'(^[\d]{4})([\d]{2})([\d]{2})$', 'Tariff Item Record'
    ),
    (
        r'(^[\d]{4})([\d]{2})$', 'Subheading Record'
    ),
    (
        r'(^[\d]{4})$', 'Chapter Heading Record'
    )
]

formatted_gather_hts_number = [
    (
        r'(^[\d]{4})\.([\d]{2})\.([\d]{2})\.([\d]{2})$', 'Statistical Suffix Record'
    ),
    (
        r'(^[\d]{4})\.([\d]{2})\.([\d]{2})$', 'Tariff Item Record'
    ),
    (
        r'(^[\d]{4})\.([\d]{2})$', 'Subheading Record'
    ),
    (
        r'(^[\d]{4})$', 'Chapter Heading Record'
    )
]

temp_hts_folder_path = '../db_hts/temp/NEW_test_files/'
hts_folder_path = '../db_hts/temp/NEW_final_json_files/'
string_folder_path = '../db_hts/temp/NEW_test_string_dict/'

raw_hts_dir_path = '../db_hts/htsdata/'
raw_hts_path = '../db_hts/htsdata/htsdata.json'

