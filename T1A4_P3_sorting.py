
#Name:Peniel Terfa Id: 101211986
from T1A_4_P1_load_data  import book_category_dictionary#importing the data


#Excercise 2
def sort_books_publisher(dictionary:dict)->list[dict]:
    book_data=[]#intializing empty list for later use
    for key in dictionary:#iterating each key in the input value
        for values in dictionary[key]:#iterating each value in the key
            book_data.append({'title':values['title'],'author':values['author'],'publisher':values['publisher'],'rating':values['rating'],'pages':values['pages'],'category':key,'language':values['language']})#appending the category as key aand other as values then appending to the empty list that we intalize on the top
    #Bubble sorting
    y=len(book_data)#creating a variable for book_data    
    for i in range(y): #going through the whole length of the data
        for j in range(0,y-i-1):#again iterating starting from the secon d value 
            book1=book_data[j]#intializing the first publisher found as one for comparing purpose
            book2=book_data[j+1]#intializing the second publisher found a second one
            if book1['publisher']>book2['publisher']:#comparing the publisher name alphebticallly the first one found to the second one 
                book_data[j],book_data[j+1]= book_data[j+1],book_data[j]#so if the first book cames letter it will not be swappped but if it is not it will be swapped
            if book1['publisher']==book2['publisher']:#comparing the publisher name alphebticallly the first one found to the second one again if they have same publisher or not
                if book1['title']>book2['title']:#comparing the title  name alphebticallly the first one found to the second one again if they have same title or not
                    book_data[j],book_data[j+1]= book_data[j+1],book_data[j]#so if the first book cames letter it will not be swappped but if it is not it will be swapped                
                       
   
    return book_data #returning the sorted file