#Name:Peniel Terfa Id :10211986
import T004_P1_book_publisher_dictionary
filename="google_books_dataset.csv"
temp=T004_P1_book_publisher_dictionary.book_publisher_dictionary(filename)
for item in temp:
    print(item,"\n")
