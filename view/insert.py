from model.movie import Movie


def insert_view(tree):
    print("Insertion\n")

    movie_id = int(input("Movie ID: "))
    movie_name = input("Name of the movie: ")
    movie_year = int(input("Movie launch year: "))

    new_movie = Movie(movie_id, movie_name, movie_year)
    try:
        tree.insert(movie_id, new_movie)
        print("Movie successfully inserted")
    except Exception as e:
        print(e)

    input("ENTER to continue")
