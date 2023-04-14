#Mushaf Wasiq 101185886
import string
from typing import List
from T1A_4_P1_load_data import book_category_dictionary

def get_books_by_category(category:str,book_category_dictionary,)->int:
    
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
    return count

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