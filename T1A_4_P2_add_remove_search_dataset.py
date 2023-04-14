import string
from typing import List
from T1A_4_P1_load_data import book_category_dictionary
from unit_testing import check_equal

#Mushaf Wasiq 101185886
def get_books_by_category(category:str,book_category_dictionary,)->list:
    """
    Returns a list of books of the desired category.
    >>>get_books_by_category('Adventure',book_category_dictionary('google_books_dataset.csv'))
    The category "Adventure" has the following books:
    1 - Sword of Destiny: Witcher 2: Tales of the Witcher
    2 - A Feast for Crows (A Song of Ice and Fire. Book 4)
    3 - After Anna
    4 - The Way Of Shadows: Book 1 of the Night Angel
    5 - A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)
    6 - Edgedancer: From the Stormlight Archive
    7 - The Malady and Other Stories: An Andrzej Sapkowski Sampler
    """    
    lst=[]
    num=0
    count=0
    for i in book_category_dictionary.keys():
        if i==category :
            books=book_category_dictionary.get(category)
            for book in books:
                lst+=[book['title']]
                count +=1
    print('The category','"'+category+'"','has',count, 'books, the following books:')
    for i in lst:
        num+=1
        print ('Book'+str(num)+':',i)
    return lst

#Mushaf Wasiq 101185886
def get_books_by_rate(dictionary:dict,rate:int)->list:
    """
    Returns a list of books within a range of ranging defined by the user
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), 3)
    There are 8 books whose rate is between 3 and 4 . This is the list of books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2: Bring Me Back by B A Paris
    Book 3: Mrs. Pollifax Unveiled by Dorothy Gilman
    Book 4: How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 5: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 6: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 7: The Infinite Game by Simon Sinek
    Book 8: Selling 101: What Every Successful Sales Professional Needs to Know by Zig Ziglar
    """       
    lst=[]
    count=0
    for i in dictionary.keys():
        cat=dictionary.get(i)
        for j in cat:
            rating=j.get('rating')
            if not rating==None:
                if rating!='N/A':
                    if rate<=rating and rating<rate+1:
                        if j not in lst:
                            lst.append(j)
    print('There are', len(lst), 'books whose rate is between', rate, 'and' ,(rate+1),'. This is the list of books:')
    for i in lst:
        count += 1
        print('Book', str(count) +':' , i.get('title'), 'by', i.get('author'))    
    return len(lst)


#Dearell Tobenna Ezeoke 101245819
def add_book(open_dictionary: dict, open_tuple: tuple) -> dict:
    """
    The function returns the updated dictionary and prints a message
    stating, “The book has been added correctly” or “There was an error
    adding the book”
    """

    if open_tuple[4] in open_dictionary:
        open_dictionary[open_tuple[4]].append(open_tuple)
        
    else:
        open_dictionary[open_tuple[4]] = [open_tuple]
    
    x = 0
    
    if open_tuple[4] in open_dictionary:
        if open_tuple in open_dictionary[open_tuple[4]]:
            x = 1
    
    if x == 0:
        print("There was an error adding the book")
    else:
        print("The book has been added correctly")
    return open_dictionary


#Dearell Tobenna Ezeoke 101245819
def remove_book(dictionary: dict, title: str, category: str) -> dict:
    """
    The function returns the updated dictionary and prints a message
    stating, “The book has been removed correctly” or “There was an error
    adding the book”
    """
    count = 0
    for key in dictionary.keys():
        if category == key:
            dic = dictionary[key]
            for book in dic:
                if title == book["title"]:
                    dic.remove(book)
                    count += 1
    if count == 1:
        print("The book has been removed correctly")
    else:
        print("There was an error removing the book. Book not found.")

    return dictionary

#Name:Peniel Terfa Id: 101211986
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

#Name:Peniel Terfa Id: 101211986
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

#Oluwatobi Olowookere 101245900
def get_books_by_title(dictionary:dict,book_title:str)-> bool:
    """
    Returns a boolean stating if a given book is in the given dictionary. Also prints out if the book is present or not.
    
    """
    count_title = 0
    answer = False
    count = 0
    for diction in dictionary:
        category_values = dictionary.values()
        for values in category_values:
            for titles in values:
                if titles["title"] == book_title:
                    answer = True
    if answer == True:
        print ("The book has been found")
    else:
        print ("The book has NOT been found")
    return answer         
    

#Oluwatobi Olowookere 101245900
def get_all_categories_for_book_title(dictionary:dict,book_title:str)->int:
    """
    Returns the number of categories a given book appears in a given dictionary.prints out the said categories
    
    """
    category_keys1 = []
    count_keys = 0
    category_keys = dictionary.keys()
    for keys in category_keys:
        for i in range(len(dictionary.get(keys))) :
            if dictionary.get(keys)[i]["title"] == book_title:
                count_keys += 1
                category_keys1 += [keys]
    print("The book title",book_title,"belongs to the following categories:")
    for i in range(len(category_keys1)):
        print("Category", i+1,":",category_keys1[i])
    return count_keys 


#Mushaf Wasiq 101185886 Testing functions 6 and 7
def check_equal(description: str, outcome, expected) -> None:
    
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")

if __name__ == "__main__":
    #Mushaf Wasiq 101185886
    #Function 6
    check_equal("get_books_by_author",get_books_by_author("author7",book_category_dictionary("test1.txt")),1)
    check_equal("get_books_by_author('Cullen Bunn',book_category_dictionary('google_books_dataset.csv'))",get_books_by_author('Cullen Bunn',book_category_dictionary('google_books_dataset.csv')),3)
    check_equal("get_books_by_author('Unknown',book_category_dictionary('google_books_dataset.csv'))",get_books_by_author('Unknown',book_category_dictionary('google_books_dataset.csv')),1)
    
    #Mushaf Wasiq 101185886
    #Function 7
    check_equal("get_books_by_publisher",get_books_by_publisher("publisher7",book_category_dictionary("test1.txt")),1)
    check_equal("Testing get_books_by_publisher(Testing'DC',book_category_dictionary('google_books_dataset.csv')", get_books_by_publisher('DC',book_category_dictionary("google_books_dataset.csv")),3)
    check_equal("Testing get_books_by_publisher(Testing'HarperCollins UK',book_category_dictionary('google_books_dataset.csv')", get_books_by_publisher('HarperCollins UK',book_category_dictionary("google_books_dataset.csv")),13)



#Dearell Tobenna Ezeoke 101245819
def test_get_books_by_title()->None:
    """
    Tests the function get_books_by_title.
    """

if __name__ == "__main__":
    print(check_equal("Testing get_books_by_title",True,get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"Antiques Roadkill: A Trash 'n' Treasures Mystery")))
    print(check_equal("get_books_by_title",get_books_by_title(book_category_dictionary("test1.txt"),"title7"),True))

#Dearell Tobenna Ezeoke 101245819
def test_get_all_categories_for_book_title()->None:
    """
    Tests the function get_all_categories_for_book_title.
    """
if __name__ == "__main__":
    print(check_equal("Testing get_all_categories_for_book_title",3,get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Antiques Roadkill: A Trash 'n' Treasures Mystery")))
    print(check_equal("get_all_categories_for_book_title",get_all_categories_for_book_title(book_category_dictionary("test1.txt"),"title7"),3))


if __name__ == "__main__":
    #Name:Peniel Terfa Id:101211986
    #Test function for three
    #One    
    check_equal("get_books_by_category('Fiction',book_category_dictionary('google_books_dataset.csv'))", get_books_by_category('Fiction',book_category_dictionary('google_books_dataset.csv')),39)
    #Two
    check_equal("get_books_by_category('Fantasy',book_category_dictionary('google_books_dataset.csv'))", get_books_by_category('Fantasy',book_category_dictionary('google_books_dataset.csv')),15)
    #Three
    check_equal("get_books_by_category('Biography',book_category_dictionary('google_books_dataset.csv'))", get_books_by_category('Biography',book_category_dictionary('google_books_dataset.csv')),7)
    
    #Name:Peniel Terfa Id:101211986
    #Test function for four
    #One
    check_equal("get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),4)", get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),4),67)
    #Two
    check_equal("get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),3)", get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),3),8)
    #Three
    check_equal("get_books_by_rate",get_books_by_rate(book_category_dictionary("test1.txt"),1.3),6)
    
if __name__ == "__main__":
    #Oluwatobi Olowookere's (101245900) review of Dearell Tobenna Ezeoke's (101245819) functions
    #Function 5
    check_equal("add_book",add_book(book_category_dictionary("test1.txt"),("title7","author8",1.3,"publisher7",237,"category3","language8")),{'category1': [{'title': 'title1', 'author': 'author1', 'language': 'language1', 'rating': 1.5, 'publisher': 'publisher1', 'pages': 233}, {'title': 'title7', 'author': 'author5', 'language': 'language5', 'rating': 1.6, 'publisher': 'publisher5', 'pages': 235}], 'category2': [{'title': 'title2', 'author': 'author2', 'language': 'language2', 'rating': 1.3, 'publisher': 'publisher2', 'pages': 232}, {'title': 'title7', 'author': 'author6', 'language': 'language6', 'rating': 1.4, 'publisher': 'publisher6', 'pages': 236}], 'category3': [{'title': 'title3', 'author': 'author3', 'language': 'language3', 'rating': 1.2, 'publisher': 'publisher3', 'pages': 233}, {'title': 'title4', 'author': 'author4', 'language': 'language4', 'rating': 1.3, 'publisher': 'publisher4', 'pages': 234}, {'title': 'title7', 'author': 'author7', 'language': 'language7 ', 'rating': 1.3, 'publisher': 'publisher7', 'pages': 237}], 237: [('title7', 'author8', 1.3, 'publisher7', 237, 'category3', 'language8')]})
    
    #Function 8
    check_equal("remove_book",remove_book(book_category_dictionary("test1.txt"),"title7","category3"),{'category1': [{'title': 'title1', 'author': 'author1', 'language': 'language1', 'rating': 1.5, 'publisher': 'publisher1', 'pages': 233}, {'title': 'title7', 'author': 'author5', 'language': 'language5', 'rating': 1.6, 'publisher': 'publisher5', 'pages': 235}], 'category2': [{'title': 'title2', 'author': 'author2', 'language': 'language2', 'rating': 1.3, 'publisher': 'publisher2', 'pages': 232}, {'title': 'title7', 'author': 'author6', 'language': 'language6', 'rating': 1.4, 'publisher': 'publisher6', 'pages': 236}], 'category3': [{'title': 'title3', 'author': 'author3', 'language': 'language3', 'rating': 1.2, 'publisher': 'publisher3', 'pages': 233}, {'title': 'title4', 'author': 'author4', 'language': 'language4', 'rating': 1.3, 'publisher': 'publisher4', 'pages': 234}]})
    
    



