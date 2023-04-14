# Myra Osima, 101249868 Id:101249868
from T1A5_P1_load_data import book_category_dictionary

# Function 5
def get_books_by_title(dictionary: dict, title: str) -> bool:
    
    """
     Returns True if the title of the book exists in the dictionary otherwise, it returns False
    >>> get_books_by_title(dictionary, "After Anna")
    the book, After Anna, has been found
    
    >>> get_books_by_title(dictionary, "Pride and Prejudice")
    the book, Pride and Prejudice, has not been found
    
    >>> get_books_by_title(dictionary, "Rework")
    the book, Rework, has been found
    """
    
    for category in dictionary.keys():
        book_list = dictionary.get(category)
        for book in book_list:
            if title == book["title"]:
                print("The  book has been found")
                return True
    print( "The book has not been found") 
    return False


"""# Function 6
def get_books_by_author(dictionary: dict, author: str) -> int:
     
    Returns the number of books written by the author and prints all titles by that author
    >>> get_books_by_author(dictionary, "John Grisham")
    
    
    >>> get_books_by_author(dictionary, "Agatha Christie")
    
    
    >>> get_books_by_author(dictionary, "Billy Ray Cyrus")
    
   
    book_title = []
    
    for category in dictionary.keys():
        book_list = dictionary.get(category)
      
        count = 0
        for book in book_list:
            if author == book["author"]:
                count += 1
            book_list.append((book['title'],book['rating']))   
                      
            
    return book_list

get_books_by_author(book_category_dictionary("google_books_dataset.csv"), "Barbara Allan")"""
#Function 6
def get_books_by_author(author_name:str, dataset:dict)->int:
    """
    Given the name of an author, the function will return the number of books written by the author and prints all the title by the given author:
    The author ___ has published the following books:
    Book 1: "Title", rate: "rating"
    Book 2: "Title", rate: "rating"
   
    >>>get_books_by_author('Barbara Allan', book_category_dictionary('google_books_dataset.csv'))
    The author "Barbara Allan" has published the following books:
    Book1:Antiques Roadkill: A Trash 'n' Treasures Mystery: Rating:3.3
    1
   
    >>>get_books_by_author('Blake Pierce', book_category_dictionary('google_books_dataset.csv'))
    The book has NOT been found
    0    
    """
   
    num_books = 0
   
    print (f'\n\nThe author "{author_name}" has published the following books:')
   
    cat_list = dataset.keys()
       
    found = False
    found_books = {}
    # For each category
    for cat in cat_list:
        books = dataset.get(cat)
       
        # for each book
        i=0
        for x in books:
            book_dict = books[i]
            i+=1
           
            # Check if the title matches        
            if author_name in book_dict.values():
                found = True
                title = book_dict['title']
                rating = book_dict['rating']
                # print (f'Found: "{title}", Rating: {rating}, in {cat}')
                # Add to the set of found books  (dupl title will be ignored)
                found_books[title]=rating
               
           
    if not found:
        print (f'\nThe book has NOT been found')    
    else:
        #print(found_books)
        i=1
        for title,rating in found_books.items():
            print (f'Book{i}:{title}: Rating:{rating}')
            i+=1
   
    # print (f'{i-1} Books found')
    # Return the number of books found
    return (i-1)
