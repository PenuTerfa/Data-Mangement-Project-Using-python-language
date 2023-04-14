#Dearell Tobenna Ezeoke 101245819

def book_category_dictionary(filename) -> dict:
    """
    Returns a dictionary in which the categories are the keys for each book.
    >>>book_category_dictionary("google_books_dataset.csv")
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'pages': '544', 'language': 'English'},... 

    """
    infile = open(filename,"r")
    lst = []
    category = {}
    count = 0
    for line in infile:
        header1=line.split(",")
        book = {}
        if count == 0:
            count += 1
        else:
            
            if header1[5] not in category:
                category[header1[5]]=[]
            if header1[2]!="N/A":#checking if the second index if it has 'N/A 'string value or not
                header1[2]=float(header1[2])            
 
            book = {'title':header1[0],'author':header1[1],'language':header1[6].strip("\n"),'rating':header1[2],'publisher':header1[3],'pages':int(header1[4])}
            category[header1[5]].append(book)

 
    infile.close() 
    return category    

