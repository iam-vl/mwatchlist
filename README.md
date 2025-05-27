# mwatchlist

* Movie wishlist, release dates
* Store the movies the user watched 

Feats: 

* Add movie 
* View upcoming movies 
* View all moviewa 
* Add a watched movie 
* View watched movies 
* Add user to the app 
* Exit  

## R1: one table 

* Can add movie to a table
* Can mark movies as watched 
* No multiple users 

```sql
UPDATE users SET first_name = 'John' WHERE surname = 'Smith';
DELETE FROM movies; -- Delete all
DELETE FROM users WHERE surname = 'Smith';
```

# R2: two tables 

```sql 
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    surname TEXT
);
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    holder_id INTEGER,
    number TEXT,
    FOREIGN KEY(holder_id) REFERENCES users(id)
);
```

# R3: Three tables 

Can do this, but not needing it. 
```
INTEGER PRIMARY KEY AUTOINCREMENT
```
