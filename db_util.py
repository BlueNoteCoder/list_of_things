import sqlite3
from sqlite3 import Error


def create_connection(file_name):
    connection = None

    try:
        connection = sqlite3.connect(file_name)
    except Error as e:
        print(e)

    print('Connection was made')

    return connection


# TODO: Create an add book to database function
# TODO: Create a function to make the necessary tables if needed

class DBUtil:
    file_extension = '.sqlite'

    def __init__(self, *args):
        if len(args) == 0:
            self.db_file_name = self.set_db_file_name()

        elif len(args) == 1:
            self.db_file_name = args[0] + DBUtil.file_extension

        create_connection(self.db_file_name)

    def get_db_file_name(self):
        print(self.db_file_name)

    def set_db_file_name(self):
        # Returns the name of the db file
        return 'book_db' + DBUtil.file_extension

    # def add_book_to_db(self, title, author):
