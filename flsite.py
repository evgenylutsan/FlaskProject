from tkinter import Menu
from flask import Flask, render_template, request, g, abort, flash, send_file
import sqlite3
import os

from matplotlib.pyplot import show, title
from FDataBase import FDataBase

DATABASE = '/tmp/books.db'
DEBUG = True
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
PREWIEW_FOLDER = os.path.join('static', 'img')
MAX_CONTENT_LENGTH = 1024 * 1024
DOWNLOAD_FOLDER = os.path.join('books')


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'books.db')))
app.config['UPLOAD_FOLDER'] = PREWIEW_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

menu = ["Главная"]


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu = menu, books = dbase.getBooksAnonce())

@app.route("/<int:id_book>")
def showBook(id_book):
    db = get_db()
    dbase = FDataBase(db)
    title, book, num_pages, size, f_ext = dbase.getBook(id_book)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'prewiew - ' + title + '.png')
    return render_template('about.html', menu = menu,title = title, book = book, num_pages = num_pages, size = size, f_ext = f_ext, img = full_filename)

@app.route('/download')
def download():
    path = os.path.join(app.config['DOWNLOAD_FOLDER'], 'Лутц Марк_Изучаем Python.pdf')

    return send_file( path, as_attachment=True)



if __name__ == "__main__":
    app.run(debug=True)


