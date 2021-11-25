from subprocess import call
from os import name

class Utilities:
    book_status = {'y': 'Read', 'n': 'Not Read'}
    own_status = {'y': 'Yes', 'n': 'No'}

    def __init__(self):
        print('Utilities created')

    # Returns the number of books in a database
    def count_num_of_books_in_db(self, db) -> int:
        books = db.get_entries()
        num_of_books = 0

        for book in books:
            num_of_books += 1

        return num_of_books

    def get_book_info(self, book_id, db) -> list:

        return db.get_entry(book_id)

    def get_all_book_info(self, db) -> list:
        return db.get_entries()

    def add_book(self, title: str, series: str, author: str, read_status: str, own_status: str, db) -> None:
        # Implement default for read_status if user leaves it blank

        if title == "" and series == "" and author == "":
            return

        if not series:
            series = 'N/A'

        db.add_book_to_db(title, series, author, Utilities.book_status[read_status], Utilities.own_status[own_status])
        print('Added Book!')
        # Maybe log that the book has been added.

    def update_book(self, book_info: list, db) -> None:

        if book_info:
            info = ['New Book Title: ', 'NEW Series', 'New Author: ', 'New Read Status(y/n): ', 'New Own Status(y/n): ']
            count = 0
            book_id, book_title, series, author, read_status, own_status = book_info

            print('\nPrevious book info will be shown below.'
                  '\nLeave row blank if you want to keep previous entry.'
                  '\n\nOLD Book Title: {title}'
                  '\nOLD Series: {series_name}'
                  '\nOLD Author: {name}'
                  '\nOLD Read Status: {r_status}'
                  '\nOLD Own Status: {o_status}\n'.format(title=book_title, series_name=series, name=author,
                                                          r_status=read_status, o_status=own_status))
            while count < len(info):
                user_input = input(info[count])

                if user_input:
                    if count + 1 == 1:  # ID
                        book_title = user_input
                    elif count + 1 == 2:  # Series
                        series = user_input
                    elif count + 1 == 3:  # Author
                        author = user_input
                    elif count + 1 == 4:  # Read/Not Read
                        read_status = Utilities.book_status[user_input]
                    elif count + 1 == 5:  # Own/Not Own
                        own_status = Utilities.own_status[user_input]
                count += 1

            db.update_book_in_db([book_id, book_title, series, author, read_status, own_status])
        else:
            print('No valid Book Information')

    # TODO: Transfer tuple conversion into list to db.get_ids function
    def delete_book(self, id: int, db) -> None:
        ids = db.get_ids()
        ids = [item[0] for item in ids]

        if id in ids:
            db.delete_book_in_db(id)
        else:
            print('{} is not a valid id'.format(id))

    def num_of_columns(self, entries) -> int:
        count = 0

        for entry in entries:
            for column in entry:
                count += 1
            break

        return count

    def largest_length_of_word_in_columns(self, db) -> list:
        """Stores length of largest word in each column into a list"""
        largest_words = []
        column = 0
        count = 1 # 0 is ID column
        entries = db.get_entries()

        while column < self.num_of_columns(entries):
            largest_length = 10
            entry_num = 0  # first entry


            while entry_num < len(entries):
                if type(entries[entry_num][column]) == int:
                    if entries[entry_num][column] > largest_length:
                        largest_length = entries[entry_num][column]

                else:
                    if len(entries[entry_num][column]) > largest_length:
                        largest_length = len(entries[entry_num][column])

                entry_num += 1

            largest_words.append(largest_length + 5)

            column += 1

        return largest_words

    def new_page(self):
        """Clears any info on terminal"""
        _ = call('clear' if name == 'posix' else 'cls')

if __name__ == '__main__':
    from db_util import DBUtil
    db = DBUtil()
    util = Utilities()
    print(util.largest_length_of_word_in_columns(db))