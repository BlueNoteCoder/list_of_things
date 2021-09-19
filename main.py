import sys

from db_util import DBUtil
from utilities import Utilities
from menu import Menu
from menu import spaces

# TODO: Add comments as necessary
# TODO: Create a function to make list of books appear neat
# TODO: Fix issue where id in database doesn't decrement after entry is deleted
# TODO: Destinquish whether its a book you want to/have read
menu = Menu()
utilities = Utilities()
db = DBUtil()

books_read = []
user_choices = {0: exit,
                1: menu.list_books_page,
                2: menu.add_book_prompt,
                3: menu.delete_book_prompt}


# Entries are centered in each column
def list_all_entries(user_selection, db):
    user_choices[user_selection]()
    books = utilities.get_all_book_info(db)
    num_spaces = spaces()
    # print(' ' + book[0] + ' ' * (num_spaces - (len(book[0]) + 2)) + book[1])
    if books:
        for book in books:
            print(' ' * (num_spaces[0] / 2) + str(book[0]) +
                  ' ' * (num_spaces[1] - num_spaces[0]) + book[1] + ' ' * (num_spaces[1] - len(book[1]) - 6) +
                  book[2])
    else:
        print('There are no books stored.\nPerhaps some reading is in store')


# TODO: Ask user if they want to make another action
def main():
    keep_loopin = True

    while keep_loopin:
        menu.print_main_menu()
        user_input = input('\nSelection: ')

        if user_input == 0:
            user_choices[user_input]("\nKeep on reading!\n")

        if user_input == 1:
            list_all_entries(user_input, db)

        elif user_input == 2:
            book_title, author = user_choices[user_input]()
            utilities.add_book(book_title, author, db)

        elif user_input == 3:
            book_id = user_choices[user_input]()
            utilities.delete_book(book_id, db)


if __name__ == '__main__':
    main()
