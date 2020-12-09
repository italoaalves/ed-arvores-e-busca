def search_year_view(tree):
    print("Search by year\n")
    movie_year = int(input("Movie year: "))

    movies = tree.search_by_year(movie_year)

    print(f"Filmes do ano {movie_year}:")
    for movie in movies:
        print(movie.name)
    input("ENTER to continue")
