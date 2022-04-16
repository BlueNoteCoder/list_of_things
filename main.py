from util.db_util import DBUtil
from util.utilities import Utilities
from util.menu import Menu
from util.menu import spaces
import logging

# TODO: Add comments as necessary
# TODO: Fix issue where id in database doesn't decrement after entry is deleted
menu = Menu()
utilities = Utilities()
db = DBUtil()

user_choices = {0: exit,
                1: menu.list_books_page,
                2: menu.add_book_prompt,
                3: menu.delete_book_prompt,
                4: menu.update_entry_prompt}


# Entries are centered in each column
def list_all_entries(user_selection: int, db) -> None:
    max_length_per_column = utilities.largest_length_of_word_in_columns(db)
    books = utilities.get_all_book_info(db)

    if books:
        user_choices[user_selection](max_length_per_column)
        for book in books:
            print(f"|{str(book[0]):^{max_length_per_column[0]}}|{book[1]:^{max_length_per_column[1]}}|"
                  f"{book[2]:^{max_length_per_column[2]}}|{book[3]:^{max_length_per_column[3]}}|"
                  f"{book[4]:^{max_length_per_column[4]}}|{book[5]:^{max_length_per_column[5]}}|")

        print('\nNumber of books: ' + str(utilities.count_num_of_books_in_db(db)))
    else:
        print('There are no books stored.\nPerhaps some reading is in store')

    print()


def main():
    logging.basicConfig(filename='logs/session.log', filemode="w", level=logging.DEBUG)

    keep_loopin = True

    while keep_loopin:
        menu.print_main_menu()
        user_input = input('\nSelection: ')

        utilities.new_page()

        if user_input == '0':
            user_choices[int(user_input)]("\nKeep on reading!\n")

        elif user_input == '1':
            list_all_entries(int(user_input), db)

        elif user_input == '2':
            book_title, series, author, read_status, own_status = user_choices[int(user_input)]()
            utilities.add_book(book_title, series, author, read_status, own_status, db)

        elif user_input == '3':
            list_all_entries(1, db)
            book_id = user_choices[int(user_input)]()

            utilities.delete_book(book_id, db)

        elif user_input == '4':
            list_all_entries(1, db)
            book_id = user_choices[int(user_input)]()

            if type(book_id) == int:
                entry = utilities.get_book_info(book_id, db)
                utilities.update_book(entry, db)
        elif user_input == '5':
            utilities.download_database(db)
        elif user_input == '6':
            user_input = input("Enter file ")
            utilities.upload_database(user_input, db)
        else:
            print('Incorrect selection, please try again!')

        input('\n**Press \'ENTER\' when ready to move on**')
        utilities.new_page()


if __name__ == '__main__':
    main()
