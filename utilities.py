class Utilities:
    def __init__(self):
        print('Utilities created')

    def add_book(self, title, author, db):

        db.add_book_to_db(title, author)
        print('Added Book!')
        # Maybe log that the book has been added.

    def get_all_book_info(self, db):
        return db.get_entries()
