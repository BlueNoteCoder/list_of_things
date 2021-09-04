def spaces():
    """Calculates the number of spaces in each column."""

    # Copied the text from the list_books_page function
    column = '|\t\t\tTITLE\t\t\t|\t\t\tAUTHOR\t\t\t|'

    num = 0
    for char in column:
        if char == '\t':
            num = num + 4
        else:
            num = num + 1

    return int(num / 2)


class Menu:
    def print_main_menu(self):
        """Prints the main actions that the user can perform"""

        print('****** Main Menu ******')
        print('-----------------------')
        print('1. View Books Read')
        print('2. Enter in a book')

    def add_book_prompt(self):
        """Will ask user for book title and author,
        then will return two"""

        book_title = input('Name of Book -> ')
        author = input('Name of Author -> ')

        return [book_title, author]

    def list_books_page(self):
        print('\n')
        print(' *' * 11 + ' BOOKS  READ ' + '* ' * 11)
        print(' ' + '-' * 55)
        print('|\t\t\tTITLE\t\t\t|\t\t\tAUTHOR\t\t\t|')


if __name__ == '__main__':
    menu = Menu()
    # menu.print_main_menu()
    # print(menu.add_book_prompt())
    menu.list_books_page()

    number = spaces()

    print(number)
