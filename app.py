import datetime

import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app. 
7) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY: ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title, timestamp)

def print_movie_list(heading, movies): 
    print(f"---{heading} MOVIES---")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} (on {human_date})")

    # for movie in movies:
    #     movie_date = datetime.datetime.fromtimestamp(movie[1])
    #     human_date = movie_date.strftime("%b %d %Y")
    #     print(f"{movie[0]}: {movie[1]} (on {human_date})")
    print("---\n")

def print_watched_movie_list(username, movies):
    print(f"-- {username}'s watched movies: --")
    for movie in movies:
        print(f"{movie[1]}")
    print("---\n")

def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie id: ")
    database.watch_movie(username, movie_id)
    # movie_title = input("Enter movie title you've watched: ")
    # database.watch_movie(username, movie_title)

def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)



while (user_input := input(menu)) != "7":
    if user_input == "1":
        print("1 OK")
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("UPCOMING", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("ALL", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        username = input("Username: ")
        movies = database.get_watched_movies(username)
        print_watched_movie_list(username, movies)
    elif user_input == "6": 
        prompt_add_user()
    else:
        print("Invalid input, please try again!")