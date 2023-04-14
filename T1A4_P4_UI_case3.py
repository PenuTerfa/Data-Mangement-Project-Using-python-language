#Name:Peniel Terfa ID:101211986
from T1A_4_P1_load_data import book_category_dictionary
import T1A_4_P2_add_remove_search_dataset 
def case3():
    """
    Load the book and then gets the book based on category and publisher what the user choose
    >>>
    
    """
    
    text='Please Enter Command Line \n\tL) Load file \n\tG) Get books \n\tC) Get books by category \n\tP) Get books by publisher \n\tQ)uit \n\n: '#interacting with the user which letter will print
    get=""
    while text!="Q":#iterating while the user enter Q to quit
        get=input(text)
        if get!="L":
            print("Error command. Please enter Command Line \n\tL) Load file \n\tG) Get books \n\tC) Get books by category \n\tP) Get books by publisher \n\tQ)uit \n\n: ")#check it and update your code
            
        elif  get.upper()=='L':
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
                                        
                    
       
        elif get.upper()=='Q':#terminating the console
            print("Done")
case3()