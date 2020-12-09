from os import system, name

from model.avl_tree import AVLTree
from view.insert import insert_view
from view.search import search_view
from view.search_year import search_year_view
from view.listing import list_view
from view.height import height_view
from view.show import show_view


options = [insert_view, search_view, search_year_view,
           list_view, height_view, show_view, quit]

# debugging
if __name__ == "__main__":

    tree = AVLTree()
    print("A new empty tree has been successfully created.")

    while True:
        system('cls' if name == 'nt' else 'clear')
        print("AVL Trees")
        print('''
        (1) Insert movie
        (2) Search movie by id
        (3) Search movies by year
        (4) List movies alphabetically
        (5) Tree height
        (6) Show tree
        (7) Exit program.
        ''')

        opt = int(input('> '))

        system('cls' if name == 'nt' else 'clear')
        options[opt-1](tree)
