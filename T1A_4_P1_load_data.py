#Written by: Dearell Tobenna Ezeoke 101245819
#Reviewed by:Peniel Terfa 101211986
#Oluwatobi Olowookere 101245900
#Muhaf Wasif 101185886	

def book_category_dictionary(filename) -> dict:
    """
    Returns a dictionary in which the categories are the keys for each book.
    >>>book_category_dictionary("google_books_dataset.csv")
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'pages': '544', 'language': 'English'},... 

    """
    infile = open(filename,"r")#opening file
    lst = []#intializing empty list for later use
    category = {}#intializing empty dictionary
    count = 0#intializing count so that later our code can skip the first line of the file
    for line in infile:
        header1=line.split(",")#removing the comma after every word
        book = {}#intializing emty list in the iteration
        if count == 0:#skipping the first line
            count += 1
        else:
            
            if header1[5] not in category:#setting category as the key
                category[header1[5]]=[]#intalizing empty list for the value
            if header1[2]!="N/A":#checking the rate value
                header1[2]=float(header1[2])#changing the rate value to float            
 
            book = {'title':header1[0],'author':header1[1],'language':header1[6].strip("\n"),'rating':header1[2],'publisher':header1[3],'pages':int(header1[4])}#putting the values inside empty dictionary
            category[header1[5]].append(book)#adding the values to the empty dictionary which have category as key

 
    infile.close() 
    return category    

