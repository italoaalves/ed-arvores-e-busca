def list_view(tree):
    print("Listing\n")

    movies = tree.list_by_name()

    if movies:
        print("Every movie in tree:")
        for movie in movies:
            print(movie)
    else:
        print("Empty tree.")

    input("ENTER to continue")
