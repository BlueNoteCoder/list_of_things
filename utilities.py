class Utilities:
    book_status = {'y': 'Read', 'n': 'Not Read'}

    def __init__(self):
        print('Utilities created')

    # Returns the number of books in a database
    def count_num_of_books_in_db(self, db):
        books = db.get_entries()
        num_of_books = 0
        
        for book in books:
            num_of_books += 1

        return num_of_books

    def get_book_info(self, book_id, db):

        return db.get_entry(book_id)

    def get_all_book_info(self, db):
        return db.get_entries()

    def add_book(self, title, author, read_status, db):
        # Implement default for read_status if user leaves it blank

        db.add_book_to_db(title, author, Utilities.book_status[read_status])
        print('Added Book!')
        # Maybe log that the book has been added.

    def update_book(self, book_info, db):
        info = ['New Book Title: ', 'New Author: ', 'New Read Status(y/n): ']
        count = 0
        book_id, book_title, author, read_status = book_info

        print('\nPrevious book info will be shown below.'
              '\nLeave row blank if you want to keep previous entry.'
              '\n\nOLD Book Title: {title}\nOLD Author: {name}\nOLD Read Status: {status}\n'.format(title=book_title, name=author, status=read_status))

        while count < len(info):
            user_input = input(info[count])

            if user_input:
                if count + 1 == 1:
                    book_title = user_input
                elif count + 1 == 2:
                    author = user_input
                elif count + 1 == 3:
                    read_status = Utilities.book_status[user_input]

            count += 1

        db.update_book_in_db([book_id, book_title, author, read_status])

    def delete_book(self, id, db):
        db.delete_book_in_db(id)

    def new_page(self):
        """Clears any info on terminal"""
        from os import system
        cls = lambda: system('cls')

        return cls()

#if __name__ == '__main__':