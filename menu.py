from os import system
from sys import platform
from subprocess import run

# TODO: Maybe return dict instead of list
def spaces() -> list:
    """Calculates the number of spaces in each column."""

    # Copied the text from the list_books_page function
    columns = '|    ID    |            TITLE            |            SERIES            |        AUTHOR        |    STATUS    |    OWN    |'
    column = columns.split('|')
    col_num = 1
    num = 0
    column_spacing = []

    while col_num < 7:  # Number of Columns is 6
        for char in column[col_num]:
            if char == '\t':
                # Terminal/Command Prompt tab spacing is 8
                num = num + 8
            else:
                num = num + 1
        column_spacing.append(num)
        num = 0
        col_num += 1

    return column_spacing


class Menu:
    # TODO: Make window size dynamically
    def set_terminal_size(self) -> None:
        """Sets window size"""
        if platform != "linux":
            system('mode con: cols=140 lines=40')
        else:
            run(["printf", "\'\e[8;40;140t\'"])  # Set terminal size to 140x40

    def get_id_from_user(self) -> int:
        """Asks for ID"""

        id = input('What is the ID of the book you wish to modify?(Hit enter to skip) -> ')

        if type(id) != int:
            return

        return int(id)

    def print_main_menu(self) -> None:
        """Prints the main actions that the user can perform"""

        # Maybe consolidate main menu into one print stmt
        print('\n****** Main Menu ******')
        print('-----------------------')
        print('0: Exit')
        print('1. View Books Read')
        print('2. Add book')
        print('3. Delete Book')
        print('4. Edit Book Info')

    def add_book_prompt(self) -> list:
        """Will ask user for book title and author,
        then will return two"""

        print('****ADD BOOK MENU****')
        print('---------------------')

        book_title = input('Name of Book -> ')
        author = input('Name of Author -> ')
        series = input('Series Name -> ')
        read_status = input('Have you read this book?(y/n) -> ')
        own_status = input('Do you own the book?(y/n) -> ')

        return [book_title, series, author, read_status, own_status]

    def delete_book_prompt(self) -> int:
        print('****DELETE BOOK MENU****')
        print('---------------------')

        return Menu.get_id_from_user(self)

    def update_entry_prompt(self) -> int:
        print('****UPDATE BOOK MENU****')
        print('------------------------')

        return Menu.get_id_from_user(self)

    def list_books_page(self, max_length_per_column) -> None:

        if max_length_per_column:
            total_length = max_length_per_column[0] + max_length_per_column[1] + max_length_per_column[2] \
                           + max_length_per_column[3] + max_length_per_column[4] + max_length_per_column[5]
        else:
            total_length = 60
            max_length_per_column = [10, 29, 30, 22, 20, 11]

        print('\n')
        print(f"{' ':<{(total_length / 2) - 2}} BOOKS!")
        # print(' *' * 25 + ' BOOKS! ' + '* ' * 25)
        print(' ' + '-' * (total_length +5))

        # |    ID    |            TITLE            |            SERIES            |        AUTHOR        |    READ STATUS    |    OWN    |
        print(f"|{'ID':^{max_length_per_column[0]}}|{'Title':^{max_length_per_column[1]}}|"
              f"{'SERIES':^{max_length_per_column[2]}}|{'AUTHOR':^{max_length_per_column[3]}}|"
              f"{'READ':^{max_length_per_column[4]}}|{'OWN':^{max_length_per_column[5]}}|")

        print(' ' + '-' * (total_length + 5))

# if __name__ == '__main__':
