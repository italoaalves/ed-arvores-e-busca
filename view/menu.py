from insert import insert_view
from search import search_view
from search_year import search_year_view
from listing import list_view
from height import height_view
from show import show_view

options = [insert_view, search_view, search_year_view, list_view, height_view, show_view, quit]

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
        
        
        
        
