#Name:Peniel Terfa ID: 101211986 

def book_publisher_dictionary(book:str)->dict:

    """
    Returns the library as a dictionary the publisher as a key and other details of book
    as values.
    
"Kensington Publishing Corp.":[ {"title": "Antiques Roadkill: A Trash 'n' Treasures
Mystery",
"author": " Barbara Allan",
"language ": "English",
"rating": 3.3,
"category": "Fiction",
"pages": 288
},
{another element},
...
],
" Pan Macmillan ":[ { "title": "The Nightshift Before Christmas: Festive hospital
diaries from the author of million-copy hit",
"author": " Adam Kay",
"language": "English",
"rating": 4.7,
"category": "Biography",
"pages": 112
},
{another element},
...
],
...
}

    """
    google_book=open(book,"r")#a variable to open our input parameter
    reader=google_book.read()#reads through our input opened file
    table={}#intializing an empty dictionary for later on use
    google=reader.split('\n')#removing the white space in the file while reading it 
    books=set()#intalizing an empty set 
    del google[0]#removing our first row of the file 
    for items in google:#iterating through the file
        char=items.split(',')#removing the commas after each word 
        if char !=['']:#while iterating through the value this is checking if the values are empty or not
            book_publisher=char[3]#intalizing the 3 index /4 column of the value as a key 
            if book_publisher not in books:#checking if there is empty value in the third index 
                table[book_publisher]=[]#intalize a empty dictionary  an empty list under it 
                books.add(book_publisher)#under the empty set that is intialized first we add every publisher on it as a key
            if char[2]!="N/A":#checking if the second index if it has 'N/A 'string value or not
                char[2]=float(char[2])#changing the second index its type to float
            table[book_publisher].append({'title': char[0], 'author': char[1], 'language': char[6], 'rating':(char[2]), 'category': char[5], 'pages': int(char[4])})#lastly  add each values that is iterated through to each publisher key while changing the pages to integer type

    return (table)#returing the apended table




