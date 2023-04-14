#Mushaf Wasiq 101185886

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

def get_books_by_title(dictionary:dict,book_title:str)-> bool:
    """
    Returns a boolean stating if a given book is in the given dictionary. Also prints out if the book is present or not.
    >>>
    
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

def options()->str:

    print('The available commands are:')
    print('1- L)oad data')
    print('2- G)et books')
    print('   T)itle R)ate A)uthor ')
    print('3- Q)uit')    

def inputs()->dict:
    """
    Gets books by title, rate ,and author based on user's input.
    """
    user_input=''
    second_input=''
    load=''
    get=''
    load_n_quit=['l','L','Q','q']
    user_inputs=['G','g','T','t','R','r','A','a']
    get_inputs=['T','t','R','r','A','a']    
    options()
    while user_input!='Q' or user_input!='q' and second_input!='Q' or second_input!='q':
        user_input=input('Enter command (Q to quit): ')
        if user_input=='Q'or user_input=='q':
            break
        elif user_input in user_inputs:
            print('Must load file first')
        elif user_input not in user_inputs and user_input not in load_n_quit:
            print('Invalid command')
        elif user_input=='L' or user_input=='l':
            load=input('Enter filename: ')
            while True:
                second_input=input('Enter command (Enter Q twice to quit): ')
                if second_input=='Q'or second_input=='q':
                    break
                elif second_input=='G' or second_input=='g':
                    get=input('How do you want to get books?: ')
                    while get not in get_inputs:
                        print('Invalid command')
                        get=input('How do you want to get books?: ')
                        if get in get_inputs:
                            break
                    if get=='a' or get=='A':
                        author=input('Enter author: ')
                        print(get_books_by_author(author,book_category_dictionary(load)))
                        options()
                    elif get=='r' or get=='R':
                        rate=int(input('Enter the rate(must be an integer): '))
                        print(get_books_by_rate(book_category_dictionary(load),rate))
                        options()
                    elif get=='t' or get=='T':
                        title=input('Enter book title: ')
                        print(get_books_by_title(book_category_dictionary(load),title))
                        options()                    
                elif second_input=='l' or second_input=='L':
                    print('File is already loaded')
                elif second_input not in user_inputs:
                    print('Invalid command')
            
inputs()            