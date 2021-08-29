from utilities import Utilities
import random
from menu import Menu
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':

books = [{'Author': 'Ben', 'Title': 'Dead'}, {'Author': 'Stu', 'Title': 'Alive'}]

gen = Utilities()
gen.add_book('Poulson', 'Blind', books)

print(books)

