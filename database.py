import datetime
import sqlite3 

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT, 
    release_timestamp REAL
);"""
CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS USERS (
    username TEXT PRIMARY KEY
);"""
CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER, 
    FOREIGN KEY (user_username) REFERENCES users(userrname),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);"""

# CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
#     watcher_name TEXT, title
# );"""



INSERT_MOVIES = """INSERT INTO movies 
    (title, release_timestamp) 
    VALUES (?, ?);
"""
INSERT_USER = """INSERT INTO users (username) VALUES(?);"""
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;" 
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;
INSERT_WATCHED_MOVIE = """INSERT INTO watched (user_username, movie_id) VALUES (?, ?);"""
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"



conn = sqlite3.connect("data.db")

def create_tables(): 
    with conn:
        conn.execute(CREATE_MOVIES_TABLE)
        conn.execute(CREATE_USERS_TABLE)
        conn.execute(CREATE_WATCHED_TABLE)

def add_movie(title, release_timestamp):
    with conn:
        conn.execute(INSERT_MOVIES, (title, release_timestamp))

def add_user():
    with conn:
        conn.execute(INSERT_USER, (username,))

def get_movies(upcoming=False):
    with conn:
        cursor = conn.cursor()
        if upcoming:
            now_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (now_timestamp,))
        else: 
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movie(username, movie_id):
    with conn:
        conn.execute(DELETE_MOVIE, (title,))
        conn.execute(INSERT_WATCHED_MOVIE, (username, movie_id))

def get_watched_movies(username):
    with conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()