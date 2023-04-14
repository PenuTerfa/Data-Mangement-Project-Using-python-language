#Name:Peniel Terfa Id: 101211986
from T1A_4_P1_load_data import book_category_dictionary
#Function 6: get_books_by_author
def get_books_by_author(author_name:str, dictionary:dict)->int:
    """
     Returns the number of books written by the authorand prints:
     The author  Barbara Allan  has published the following books:
Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery ,rate: 3.3
Book 2 : Antiques Con ,rate: 4.8
Book 3 : Antiques Chop ,rate: 4.5
Book 4 : Antiques Knock-Off ,rate: 4.3
    """
    title=[]
    rating=[]
    book_1=[]  
    count=1
    print("The author ",author_name," has published the following books:")
    for item in dictionary:
        book_1 += dictionary.get(item)
    for values in book_1:
        if author_name==values.get('author'):
            if values.get('title') not in title :
                title += [values.get('title')]
            if values.get('rating') not in rating :
                rating += [values.get('rating')]
                print('Book',count,':',values.get('title'),',rate:',values.get('rating'))
                count+=1
    return count 
#Function 7: get_books_by_publisher
def get_books_by_publisher(publisher_name:str, book_dictionary:dict)->int:
    """
    Returns the number of books published by the given publisher’s and prints :
    The publisher  AMACOM  has published the following books:
Book 1 : Marketing (The Brian Tracy Success Library) by Brian Tracy
Book 2 : Management (The Brian Tracy Success Library) by Brian Tracy
Book 3 : Business Strategy (The Brian Tracy Success Library) by Brian Tracy
Book 4 : Personal Success (The Brian Tracy Success Library) by Brian Tracy
Book 5 : The Essentials of Finance and Accounting for Nonfinancial Managers by Edward Fields
    """
    title=[]
    author=[]
    book=[]  
    count=1
    print("The publisher ",publisher_name," has published the following books:")
    for key in book_dictionary:
        book += book_dictionary.get(key)
    for values in book:
        if publisher_name==values.get('publisher'):
            if values.get('title') not in title :
                title += [values.get('title')]
                if values.get('author') not in author :
                    author += [values.get('author')]
                print('Book',count,':',values.get('title'),'by',values.get('author'))
                count+=1
    return count 

