#Name:Peniel Terfa Id:101211986
from T1A_4_P1_load_data import book_category_dictionary
import unit_testing
from T1A4_P2_fun import get_books_by_category
from T1A4_P2_fun import get_books_by_rate
#Test function for three
#One
unit_testing.check_equal("get_books_by_category('Fiction',book_category_dictionary('google_books_dataset.csv'))", get_books_by_category('Fiction',book_category_dictionary('google_books_dataset.csv')),39)
#Two
unit_testing.check_equal("get_books_by_category('Fantasy',book_category_dictionary('google_books_dataset.csv'))", get_books_by_category('Fantasy',book_category_dictionary('google_books_dataset.csv')),15)
#Three
unit_testing.check_equal("get_books_by_category('Biography',book_category_dictionary('google_books_dataset.csv'))", get_books_by_category('Biography',book_category_dictionary('google_books_dataset.csv')),7)
#Test function for four
#One
unit_testing.check_equal("get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),4)", get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),4),67)
#Two
unit_testing.check_equal("get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),3)", get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),3),8)
#Three
unit_testing.check_equal("get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),2)", get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),2),0)
