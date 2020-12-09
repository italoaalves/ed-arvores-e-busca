def search_view(tree):
    print("Search")

    movie_id = int(input("Movie ID: "))
    try:
        movie = tree.search(movie_id)

        print("Movie found:")
        print(f"Name: {movie.name}")
        print(f"Year: {movie.year}")
    except Exception as e:
        print(e)

    input("ENTER to continue")
