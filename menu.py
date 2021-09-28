# TODO: Maybe return dict instead of list
def spaces():
    """Calculates the number of spaces in each column."""

    # Copied the text from the list_books_page function
    columns = '|    ID    |            TITLE            |        AUTHOR        |    STATUS    |'
    column = columns.split('|')
    col_num = 1
    num = 0
    column_spacing = []

    while col_num < 5:
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

    def print_main_menu(self):
        """Prints the main actions that the user can perform"""

        # Maybe consolidate main menu into one print stmt
        print('\n****** Main Menu ******')
        print('-----------------------')
        print('0: Exit')
        print('1. View Books Read')
        print('2. Add book')
        print('3. Delete Book')

    def add_book_prompt(self):
        """Will ask user for book title and author,
        then will return two"""

        print('****ADD BOOK MENU****')
        print('---------------------')
        book_title = input('Name of Book -> ')
        author = input('Name of Author -> ')
        read_status = input('Have you read this book?(y/n) -> ')

        return [book_title, author, read_status]

    def delete_book_prompt(self):
        print('****DELETE BOOK MENU****')
        print('---------------------')

        return Menu.get_id_from_user(self)

    def update_entry(self):
        print('****UPDATE BOOK MENU****')
        print('------------------------')
        
        return Menu.get_id_from_user(self)


    def list_books_page(self):
        tab = 4
        print('\n')
        print(' *' * 18 + ' BOOKS! ' + '* ' * 18)
        print(' ' + '-' * 78)

        # |    ID    |            TITLE            |        AUTHOR        |    STATUS    |
        print('|' + ' ' * tab + 'ID' + ' ' * tab + '|' + ' ' * (tab * 3) + 'TITLE' + ' ' * (tab * 3) + '|'
              + ' ' * (tab * 2) + 'AUTHOR' + ' ' * (tab * 2) + '|' + ' ' * tab + 'STATUS' + ' ' * tab + '|')
        print(' ' + '-' * 78)


#if __name__ == '__main__':