import sqlite3
from sqlite3 import Error
import logging

logging.basicConfig(filename='logs/session.log', filemode="w", level=logging.DEBUG)


def create_connection(file_name):
    connection = None

    try:
        logging.info(f"Establishing connection to {file_name}")

        connection = sqlite3.connect(file_name)
    except Error as e:
        print(e)
        logging.info(e)

    logging.info(f"Connection to {file_name} has been established")

    return connection

# TODO: Move string "databases/" in init function and apply it to the set_db_file_name
# TODO: Create an add book to database function
# TODO: Create ahttps://stranded-deep.fandom.com/wiki/Rudder function to make the necessary tables if needed
# TODO: Make a variable (maybe private) to hold complete path of db file

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
            self.db_file_name = "databases/" + self.set_db_file_name()

        elif len(args) == 1:
            self.db_file_name = args[0] + DBUtil.file_extension

        logging.info("Creating database at {database}.".format(database=self.db_file_name))

        self.conn = create_connection(self.db_file_name)
        logging.info("Database created at {database}.".format(database=self.db_file_name))
        self.create_book_table()

    def get_db_file_name(self) -> str:
        return self.db_file_name

    # TODO: Fix default name + function name
    def set_db_file_name(self) -> str:
        # Returns the name of the db file
        return 'books_read_db' + DBUtil.file_extension

    # TODO: Add statement to check if table is already created. Then log if it is
    # TODO: Add option to update table
    def create_book_table(self):
        table_stmt = """CREATE TABLE IF NOT EXISTS {table_name} (
                            id integer PRIMARY KEY,
                            book_title TEXT NOT NULL,
                            series_name TEXT,
                            author_name TEXT NOT NULL,
                            read_status TEXT NOT NULL,
                            own_status TEXT NOT NULL); """.format(table_name=self.book_table)

        logging.info("Creating {table_name} table.".format(table_name=self.book_table))

        cursor = self.conn.cursor()
        # TODO: Try statement to determine whether table already exists?
        cursor.execute(table_stmt)

        # Logging: "{Book_table} has been created"
        logging.info("{table_name} table has been created.".format(table_name=self.book_table))

    def get_ids(self) -> list:
        """Returns list of all id's in database"""

        entries = []
        stmt = """SELECT id FROM {table_name}""".format(table_name=self.book_table)

        cursor = self.conn.cursor()
        cursor.execute(stmt)
        rows = cursor.fetchall()

        for row in rows:
            entries.append(row)

        # Logging: "Obtained all ids"
        return entries

    def get_entry(self, book_id: int) -> list:
        """Params:book_id
        Returns the entry of the given book_id in a list"""

        entry = []
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM {table_name} WHERE id=?".format(table_name=self.book_table), (book_id,))
        rows = cursor.fetchall()

        # Logging: "Obtaining info for ID: {id}"
        for row in rows:
            for column in row:
                entry.append(column)

        # Logging: " Obtained ID: {id} = {entry}"
        return entry

    def get_entries(self) -> list:
        """Returns list of all entries in database"""

        entries = []
        stmt = """SELECT * FROM {table_name}
                ORDER BY read_status""".format(table_name=self.book_table)

        cursor = self.conn.cursor()

        # Logging: "Obtaining all rows for {book_table}"
        cursor.execute(stmt)
        rows = cursor.fetchall()

        for row in rows:
            entries.append(row)

        # Logging: "Obtained all rows for {book_table}"
        return entries

    def add_book_to_db(self, title: str, series: str, author: str, is_read: bool, is_owned: bool) -> None:
        stmt = """INSERT INTO {table_name}(book_title, series_name, author_name, read_status, own_status)
                    VALUES(?,?,?,?,?) """.format(table_name=self.book_table)
        info = (title, series, author, is_read, is_owned)

        logging.info(f"Adding new book with following info:\n\tTitle: {title}\n\tSeries: {series}\n\tAuthor: {author}"
                     f"\n\tHas been read: {is_read}\n\tOwns Book: {is_owned}")
        cursor = self.conn.cursor()

        print('Adding book to db')
        cursor.execute(stmt, info)
        self.conn.commit()

        # Logging: "Added {book info} to ID: {id}"
        print('Added book to database')

    def update_book_in_db(self, book_info: list) -> None:
        """:param book_info is a list containing [id, title, author, read_status, own_status]"""
        book_id, title, series, author, status, own_status = book_info

        # Store old book info in list
        stmt = """UPDATE {table_name}
                SET book_title = ?,
                    series_name = ?,
                    author_name = ?,
                    read_status = ?,
                    own_status = ?
                WHERE id = ?""".format(table_name=self.book_table)

        info = (title, series, author, status, own_status, book_id)

        logging.info(f"Updating book info for ID: {book_id}")
        cursor = self.conn.cursor()
        cursor.execute(stmt, info)
        self.conn.commit()

    def delete_book_in_db(self, book_id: int) -> None:
        stmt = """DELETE FROM {table_name} WHERE id = ?""".format(table_name=self.book_table)
        cursor = self.conn.cursor()
        cursor.execute(stmt, (book_id,))
        self.conn.commit()
        logging.info(f"ID: {book_id} has been deleted")


if __name__ == "__main__":
    db = DBUtil()
    print(db.get_entry(2))
