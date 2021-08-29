class Utilities:
    def __init__(self):
        print('Utilities created')

    def add_book(self, author, title, bookList):
        bookList.append({'Author': author, 'Title': title})
