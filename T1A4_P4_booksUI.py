#Case 1:#OLUWATOBI OLOWOOKERE 101245900
#case 2 : Mushaf Wasiq 101185886
#Case 3: Name:Peniel Terfa ID:101211986
#Case 4: QDearell Tobenna Ezeoke 101245819
import string
from T1A_4_P1_load_data import book_category_dictionary
import T1A_4_P2_add_remove_search_dataset 
from T1A_4_P2_add_remove_search_dataset import add_book,remove_book
#OLUWATOBI OLOWOOKERE 101245900
def case1()->dict:
 """
 add books or remove books based on the user input
 
 """
                         
 m = input("The available commands are:"+"\n"+ "1- L)oad data"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"    "+"T)itle R)ate A)uthor P)ublisher C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"Please type your command: ")
 while  m != "Q" :
                         if m != "L":
                                                  m = input("No such command"+"\n"+"\n"+"The available commands are:"+"\n"+ "1- L)oad data"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"    "+"T)itle R)ate A)uthor P)ublisher C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"Please type your command: ").upper()
                         elif m == "L":
                                                  filename = input("Enter the name of the file to be loaded: ")
                                                  infile = open(filename,"r") 
                                                  if input("The available commands are:"+"\n"+ "1- L)oad data"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"    "+"T)itle R)ate A)uthor P)ublisher C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"Please type your command: ").upper() == "A":
                                                                           add_book(book_category_dictionary(filename), input("Enter book details: "))
                                                  elif input("The available commands are:"+"\n"+ "1- L)oad data"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"    "+"T)itle R)ate A)uthor P)ublisher C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"Please type your command: ").upper() == "R":
                                                                           remove_book(book_category_dictionary(filename), input("Enter book details: ")[0], input("Enter book details")[1]) 
                                                  m = input("The available commands are:"+"\n"+ "1- L)oad data"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"    "+"T)itle R)ate A)uthor P)ublisher C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"Please type your command: ").upper()
                         if m==Q:
                          print("The program has ended. Goodbye")
case1()
 #Mushaf Wasiq 101185886
def options()->str:

    print('The available commands are:')
    print('1- L)oad data')
    print('2- G)et books')
    print('   T)itle R)ate A)uthor ')
    print('3- Q)uit')    

def case2()->dict:
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
                        T1A_4_P2_add_remove_search_dataset.get_books_by_author(author,book_category_dictionary(load))
                        options()
                    elif get=='r' or get=='R':
                        rate=int(input('Enter the rate(must be an integer): '))
                        T1A_4_P2_add_remove_search_dataset.get_books_by_rate(book_category_dictionary(load),rate)
                        options()
                    elif get=='t' or get=='T':
                        title=input('Enter book title: ')
                        T1A_4_P2_add_remove_search_dataset.get_books_by_title(book_category_dictionary(load),title)
                        options()                    
                elif second_input=='l' or second_input=='L':
                    print('File is already loaded')
                elif second_input not in user_inputs:
                    print('Invalid command')
            
case2()            

def case3()->dict:
    """
    Load the book and then gets the book based on category and publisher what the user choose
    >>>
    
    """
    
    text='Please Enter Command Line \n\tL) Load file \n\tG) Get books \n\tC) Get books by category \n\tP) Get books by publisher \n\tQ)uit \n\n: '#interacting with the user which letter will print
    get=""
    while text!="Q":#iterating while the user enter Q to quit
        get=input(text)
        if  get.upper()=='L':
            filename = input("Enter the name of the file to be loaded: ")
            infile = open(filename,"r") 
            get=input("did you want to get books:")
            if get.upper()!='G': #checking for geeting the letter G to get books by desired
                 if filename== {}:#checking if the data is loaded or not
                    print("No file has been loaded")
                    print("Please enter L to load a file")
            else: #if it is not empty set we let the user which key he wants to find
                get=input("which one did you want to get:")
                if filename== {}:#again checing for empty set
                    print("No file has been loaded")
                    print("Please enter L to load a file")
                else:
                    if get.upper()=='C':#checking if the user wants to select the category
                        if filename == {}:#checking for empty set  again
                            print("No file has been loaded")
                            print("Please enter L to load a file")
                        else:#letting the user choose one of the category 
                            category=input("Please enter the name of the category:")
                            
                            T1A_4_P2_add_remove_search_dataset.get_books_by_category(category,book_category_dictionary(filename))
                    if get.upper()=='P':#checking if the user wants the publisher key
                        if filename == {}:#again checking for empty set
                            print("No file has been loaded")
                            print("Please enter L to load a file")
                        else:#letting the user choose which publisher he needs 
                            publisher=input("Please enter the name of the publisher:")
                            T1A_4_P2_add_remove_search_dataset.get_books_by_publisher(publisher,book_category_dictionary(filename))
                        if get.upper()=='Q':#terminating the console
                           print("Done")
case3()
#Dearell Tobenna Ezeoke 101245819

from T1A_4_P1_load_data import book_category_dictionary
from T1A_4_P3_sorting_fun import sort_books_title, sort_books_ascending_rate, sort_books_author, sort_books_publisher
from bubblebubble import bubbleSort
from T1A_4_check_equal import check_equal

def case4() ->dict:
   
    """Returns the UI for command 6 and its sub commands
    """
    load = False
    menu = input("The available commands are:"+"\n"+ "1- L)oad data"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"       "+"T)itle   R)ate   A)uthor   P)ublisher   C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"6- S)ort books"+"\n" + "       T)itle   R)ate   P)ublisher   A)uthor " +"\n"+ "7- Q)uit"+"\n"+"Please type your command: ").upper()
    
    while menu != "Q": 
        if menu == "L":
            loaded_dic = input("Enter the name of the file to be loaded: ")
            load_data = book_category_dictionary(loaded_dic)
            load = True
    
        if load==True:
            menu = input("The available commands are:"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"    "+"T)itle   R)ate   A)uthor   P)ublisher   C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"6- S)ort books"+"\n" + "    T)itle   R)ate   P)ublisher   A)uthor " +"\n"+ "7- Q)uit"+"\n"+"Please type your command: ").upper() 
            
            if menu == "S":
                sub = input("T)itle   R)ate   P)ublisher   A)uthor" + "\n" + "Please type your command: ").upper()
                if sub == "T":
                    print(sort_books_title(book_category_dictionary("google_books_dataset.csv")))
                   
             
                elif sub == "R":
                    print(sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv")))
                 
             
                elif sub == "P":
                    print(sort_books_publisher(book_category_dictionary("google_books_dataset.csv")))
                   
                       
                elif sub == "A":
                    print(sort_books_author(book_category_dictionary("google_books_dataset.csv")))
                elif menu == "Q":
                    print("The program has ended. Goodbye.")                
                   
                else:
                    print("No such command") 
                       
            elif menu == "Q":
                print("The program has ended. Goodbye.")   
            elif menu !="S" or "Q":
                print("No such command")             
        elif menu != "L":
            print("No file loaded")
            menu = input("The available commands are:"+"\n"+ "1- L)oad data"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"    "+"T)itle   R)ate   A)uthor   P)ublisher   C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"6- S)ort books"+"\n" + "    T)itle   R)ate   P)ublisher   A)uthor " +"\n"+ "7- Q)uit"+"\n"+"Please type your command: ").upper()     
                           

        else:
            print("No such command")
            
case4()