#OLUWATOBI OLOWOOKERE 101245900
import string
from T1A_4_P1_load_data import book_category_dictionary
from T1A_4_P2_add_remove_search_dataset import add_book,remove_book

m = input("The available commands are:"+"\n"+ "1- L)oad data"+"\n"+"2- A)dd book"+"\n"+"3- R)emove book"+"\n"+"4- G)et books"+"\n"+"    "+"T)itle R)ate A)uthor P)ublisher C)ategory"+"\n"+"5- GCT) Get all Categories for book Title"+"\n"+"Please type your command: ").upper()
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
if m == "Q":
                         print("The program has ended. Goodbye")
                         
                         
                                                                           


                         