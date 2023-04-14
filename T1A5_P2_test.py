#Name:Myra Osmia ID: 101249868
from T1A5_P1_load_data import book_category_dictionary
import unit_testing
from T1A5_P2_fun import get_books_by_title
from T1A5_P2_fun import get_books_by_author
#For fun 5
#1
unit_testing.check_equal("get_books_by_title(book_category_dictionary('google_books_dataset.csv'),'Antiques Roadkill: A Trash 'n' Treasures Mystery'", get_books_by_title(book_category_dictionary('google_books_dataset.csv'),'Antiques Roadkill: A Trash "n"Treasures Mystery'),False)
#2
unit_testing.check_equal("get_books_by_title(book_category_dictionary('google_books_dataset.csv'),'Total Control'", get_books_by_title(book_category_dictionary('google_books_dataset.csv'),'Total Control'),True)
#3
unit_testing.check_equal("get_books_by_title(book_category_dictionary('google_books_dataset.csv'),'The Mysterious Affair at Styles'", get_books_by_title(book_category_dictionary('google_books_dataset.csv'),'The Mysterious Affair at Styles'),True)
#For fun 6
#1
unit_testing.check_equal("get_books_by_author('Blake Pierce',book_category_dictionary('google_books_dataset.csv')", get_books_by_author('Blake Pierce',book_category_dictionary('google_books_dataset.csv')),6)
#2
unit_testing.check_equal("get_books_by_author('David Allen',book_category_dictionary('google_books_dataset.csv')", get_books_by_author('David Allen',book_category_dictionary('google_books_dataset.csv')),1)
#3
unit_testing.check_equal("get_books_by_author('Alvin Hall',book_category_dictionary('google_books_dataset.csv')", get_books_by_author('Alvin Hall',book_category_dictionary('google_books_dataset.csv')),1)

