def spaces():
    """Calculates the number of spaces in each column."""

    # Copied the text from the list_books_page function
    columns = '|\tID\t|\t\tTITLE\t\t|\t\tAUTHOR\t\t|'
    column = columns.split('|')
    col_num = 1
    num = 0
    column_spacing = []

    while col_num < 4:
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

        book_title = input('Name of Book -> ')
        author = input('Name of Author -> ')

        return [book_title, author]

    def delete_book_prompt(self):
        """Asks user to look at the list of books already in the
        the table to gather ID number of book to delete.

        Next, asks for ID and returns it"""

        print('REMINDER: Need ID from the list of books to'
              '\nbe able to delete the book')
        id = input('What is the ID number? -> ')

        return id


    def list_books_page(self):
        print('\n')
        print(' *' * 17 + ' BOOKS  READ ' + '* ' * 17)
        print(' ' + '-' * 79)
        print('|\tID\t|\t\tTITLE\t\t|\t\tAUTHOR\t\t|')


#if __name__ == '__main__':
