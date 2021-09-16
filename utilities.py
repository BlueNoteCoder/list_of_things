class Utilities:
    def __init__(self):
        print('Utilities created')

    # Returns the number of books in a database
    def count_num_of_books_in_db(self, db):
        books = db.get_entries()
        num_of_books = 0

        for book in books:
            num_of_books += 1

        return num_of_books

    def get_all_book_info(self, db):
        return db.get_entries()

    def add_book(self, title, author, db):

        db.add_book_to_db(title, author)
        print('Added Book!')
        # Maybe log that the book has been added.

# if __name__ == '__main__':
