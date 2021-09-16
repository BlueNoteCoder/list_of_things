import sqlite3
from sqlite3 import Error


def create_connection(file_name):
    connection = None

    try:
        print('Establishing a connection')

        connection = sqlite3.connect(file_name)
    except Error as e:
        print(e)

    print('Connection was made')

    return connection


# TODO: Create an add book to database function
# TODO: Create a function to make the necessary tables if needed

class DBUtil:
    """DBUtil class is written for sqlite
    """

    # Specify what extension you want the db to be
    file_extension = '.db'

    def __init__(self, *args):

        """ When DBUtil is initialized, it will look for an argument to
        name the db file.
        If no argument is provided, then it will assign the file name.
        """

        self.book_table = 'books_read'

        if len(args) == 0:
            self.db_file_name = self.set_db_file_name()

        elif len(args) == 1:
            self.db_file_name = args[0] + DBUtil.file_extension

        self.conn = create_connection(self.db_file_name)

        self.create_book_table()

    def get_db_file_name(self):
        return self.db_file_name

    def set_db_file_name(self):
        # Returns the name of the db file
        return 'books_read_db' + DBUtil.file_extension

    # TODO: Add statement to check if table is already created. Then log if it is
    def create_book_table(self):
        table_stmt = """CREATE TABLE IF NOT EXISTS {table_name} (
                            id integer PRIMARY KEY,
                            book_title TEXT NOT NULL,
                            author_name TEXT NOT NULL); """.format(table_name=self.book_table)

        print('Creating Database')

        cursor = self.conn.cursor()
        cursor.execute(table_stmt)

        print('Database Created')

    def get_entries(self):
        entries = []
        stmt = """SELECT * FROM {table_name}""".format(table_name=self.book_table)

        cursor = self.conn.cursor()
        cursor.execute(stmt)
        rows = cursor.fetchall()

        for row in rows:
            entries.append(row)

        return entries

    def add_book_to_db(self, title, author):
        stmt = """INSERT INTO {table_name}(book_title, author_name)
                    VALUES(?,?) """.format(table_name=self.book_table)
        info = (title, author)
        cursor = self.conn.cursor()

        print('Adding book to db')
        cursor.execute(stmt, info)
        self.conn.commit()
        print('Added book to database')

    def delete_book_in_db(self, book_id):
        stmt = """DELETE FROM {table_name} WHERE id = ?""".format(table_name=self.book_table)

        cursor = self.conn.cursor()

        print('Deleting book')
        cursor.execute(stmt, (book_id,))
        self.conn.commit()
        print('Deleted book')


if __name__ == "__main__":
    db = DBUtil()
    db.delete_book_in_db(1)