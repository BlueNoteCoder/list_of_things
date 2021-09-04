from db_util import DBUtil
from utilities import Utilities
from menu import Menu
from menu import spaces

# TODO: Add comments as necessary
# TODO: Create a function to make list of books appear neat
menu = Menu()
utilities = Utilities()
db = DBUtil()

books_read = []
user_choices = {1: menu.list_books_page, 2: menu.add_book_prompt}


def list_all_entries(user_selection, db):
    user_choices[user_input]()
    books = utilities.get_all_book_info(db)
    num_spaces = spaces()

    if books:
        for book in books:
            print(' ' + book[0] + ' ' * (num_spaces - (len(book[0]) + 2)) + book[1])
    else:
        print('There are no books stored.\nPerhaps some reading is in store')


if __name__ == '__main__':

    menu.print_main_menu()

    while True:

        user_input = int(input())

        if user_input == 1:
            list_all_entries(user_input, db)

        elif user_input == 2:
            book_title, author = user_choices[user_input]()
            utilities.add_book(book_title, author, db)
