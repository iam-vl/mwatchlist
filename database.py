import datetime
import sqlite3 

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT, 
    release_timestamp REAL, 
    watched INTEGER
);
"""

INSERT_MOVIES = """INSERT INTO movies 
    (title, release_timestamp, watched) 
    VALUES (?, ?, 0);
"""

SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;" 
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"



conn = sqlite3.connect("data.db")

def create_tables(): 
    with conn:
        conn.execute(CREATE_MOVIES_TABLE)

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

def watch_movie():
    pass
def get_watched_movies():
    pass