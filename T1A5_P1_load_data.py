# Rory Bartlett 101220840 (Original Writer of the Code)
# Myra Osima 101249868 (Reviewer)
# Falkon Farhat 101222167 (Reviewer)
# David Madumere 101202744 (Reviewer)

def book_category_dictionary(file:str)->dict:
    """
    Opens a csv file book list and creates a category-based dictionary of the books contained in the file. 
    
    >>> print ( book_category_dictionary('google_books_dataset.csv') )
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'pages': '288'}    
    
    """
    csv_file = open('google_books_dataset.csv', 'r')
    result_dic = {}
    count = 0
    for line in csv_file:
        row = line.split(',')
        if count == 0:
            header = row
            count+=1
        else:
            book = {}
            if row[5] not in result_dic:
                result_dic[row[5]]=[]
            book[header[0]] = row[0]
            book[header[1]] = row[1]
            book[header[2]] = row[2]
            book[header[3]] = row[3]
            book[header[4]] = row[4]
            book[header[6]] = row[6] 
            result_dic[row[5]].append(book)
                 
    return result_dic
