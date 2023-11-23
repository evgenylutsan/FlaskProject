# import sqlite3
# from flask import url_for
# from psycopg2 import connect

# db = sqlite3.connect('books.db')
# cur = db.cursor()

# cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title varchar(100) UNIQUE, author varchar(100) UNIQUE, num_pages int UNIQUE ,size varchar(100) UNIQUE, f_ext varchar(100) UNIQUE, prewiew BLOB)")
# db.commit()

# cur.execute("CREATE TABLE comment (comment varchar(100) UNIQUE, BookId INTEGER,  FOREIGN KEY (BookId)  REFERENCES books (id))")
# db.commit()



