from view.insert import insert_view
from view.search import search_view
from view.search_year import search_year_view
from view.listing import list_view
from view.height import height_view
from view.show import show_view

options = [insert_view, search_view, search_year_view,
           list_view, height_view, show_view, quit]


def menu_view():
    while True:
        print('''
        (1) Inserir filme
        (2) Buscar filme pelo id
        (3) Buscar filmes pelo ano
        (4) Listar filmes em ordem alfabética
        (5) Altura da árvore
        (6) Exibir a árvore
        (7) Sair do programa.
        ''')

        opt = int(input('> '))

        options[opt-1]()


# debugging
if __name__ == "__main__":
    menu_view()
