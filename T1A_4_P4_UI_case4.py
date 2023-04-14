#Dearell Tobenna Ezeoke 101245819

from T1A_4_P1_load_data import book_category_dictionary
from T1A_4_P3_sorting_fun import sort_books_title, sort_books_ascending_rate, sort_books_author, sort_books_publisher
from bubblebubble import bubbleSort
from T1A_4_check_equal import check_equal

def case4() ->None:
    """
    Returns the UI for command 6 and its sub commands
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