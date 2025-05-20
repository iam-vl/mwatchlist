import datetime
import sqlite3 

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT, 
    release_timestamp REAL
);
"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (watcher_name TEXT, title);"""
INSERT_WATCHED_MOVIE = """INSERT INTO watched (watcher_name, title) VALUES (?, ?);"""

INSERT_MOVIES = """INSERT INTO movies 
    (title, release_timestamp) 
    VALUES (?, ?);
"""

SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;" 
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"



conn = sqlite3.connect("data.db")

def create_tables(): 
    with conn:
        conn.execute(CREATE_MOVIES_TABLE)
        conn.execute(CREATE_WATCHLIST_TABLE)

def add_movie(title, release_timestamp):
    with conn:
        conn.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with conn:
        cursor = conn.cursor()
        if upcoming:
            now_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (now_timestamp,))
        else: 
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movie(username, title):
    with conn:
        conn.execute(DELETE_MOVIE, (title,))
        conn.execute(INSERT_WATCHED_MOVIE, (username, title))

def get_watched_movies(username):
    with conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()