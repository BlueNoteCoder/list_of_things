import csv
from subprocess import call
from os import name
import logging

logging.basicConfig(filename='logs/session.log', filemode="w", level=logging.DEBUG)


class Utilities:
    book_status = {'y': 'Read', 'n': 'Not Read', 'ip': 'In Progress'}
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
            info = ['New Book Title: ', 'NEW Series:', 'New Author: ', 'New Read Status(y/n/ip): ', 'New Own Status(y/n): ']
            count = 0
            book_id, book_title, series, author, read_status, own_status = book_info

            logging.info(f" Old info of book: \n\tBook: {book_title}\n\tSeries: {series}\n\tAuthor: {author}"
                         f"\n\tHas read book: {read_status}\n\tOwns books: {own_status}")

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
            logging.info(f"Book ID of {book_id} has been updated with:\n\tBook: {book_title}\n\tSeries: {series}"
                         f"\n\tAuthor: {author}\n\tHas read book: {read_status}\n\tOwns books: {own_status}")
        else:
            print('No valid Book Information')

    # TODO: Transfer tuple conversion into list to db.get_ids function
    def delete_book(self, id: int, db) -> None:
        ids = db.get_ids()
        ids = [item[0] for item in ids]

        if id in ids:
            logging.info(f"Removing ID: {id} with the following information: {db.get_entry(id)}")
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
        count = 1  # 0 is ID column
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

    def download_database(self, db):
        with open('../list_of_things/downloaded_table.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Title', 'Author', 'Series', 'Read', 'Own'])
            writer.writerows(db.get_entries())

    def upload_database(self, file: str, db):
        data_from_csv = []

        if ".csv" not in file:
            print("File needs to be a csv format!")
            return

        with open(file, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                data_from_csv.append(row)

        if len(data_from_csv[0]) != 5:
            print("Table doesn't have the right columns")

        for i in range(1, len(data_from_csv)):
            if "Read" not in data_from_csv[i][3] and "Not Read" not in data_from_csv[i][3]:
                print("Read Status is not in vaild format")
                continue
            elif "Yes" not in data_from_csv[i][4] and "No" not in data_from_csv[i][4]:
                print("Own status is not in vaild format")
                continue
            else:
                print("csv file is in valid format")

            db.add_book_to_db(data_from_csv[i][0], data_from_csv[i][1], data_from_csv[i][2], data_from_csv[i][3], data_from_csv[i][4])
        print("Valid csv file")
    # reader = csv.reader()


if __name__ == '__main__':
    from db_util import DBUtil

    db = DBUtil()
    util = Utilities()
    print(util.largest_length_of_word_in_columns(db))
