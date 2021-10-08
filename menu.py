# TODO: Maybe return dict instead of list
def spaces():
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
    def get_id_from_user(self):
        """Asks for ID"""

        id = input('What is the ID of the book you wish to modify? -> ')

        return int(id)

    def print_main_menu(self):
        """Prints the main actions that the user can perform"""

        # Maybe consolidate main menu into one print stmt
        print('\n****** Main Menu ******')
        print('-----------------------')
        print('0: Exit')
        print('1. View Books Read')
        print('2. Add book')
        print('3. Delete Book')
        print('4. Edit Book Info')

    def add_book_prompt(self):
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

    def delete_book_prompt(self):
        print('****DELETE BOOK MENU****')
        print('---------------------')

        return Menu.get_id_from_user(self)

    def update_entry_prompt(self):
        print('****UPDATE BOOK MENU****')
        print('------------------------')

        return Menu.get_id_from_user(self)

    def update_entry(self,):
        print('****UPDATE BOOK MENU****')
        print('------------------------')

    def list_books_page(self):
        tab = 4
        print('\n')
        print(' *' * 30 + ' BOOKS! ' + '* ' * 30)
        print(' ' + '-' * 127)

        # |    ID    |            TITLE            |            SERIES            |        AUTHOR        |    READ STATUS    |    OWN    |
        print(f"|{'ID':^10}|{'AUTHOR':^29}|{'SERIES':^30}|{'AUTHOR':^22}|{'READ':^20}|{'OWN':^11}|")

        print(' ' + '-' * 127)

#if __name__ == '__main__':