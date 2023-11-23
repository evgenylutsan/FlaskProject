from msilib.schema import Error
import sqlite3
from flask import url_for
from matplotlib.pyplot import title

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getBook(self, bookId):
        try:
            self.__cur.execute(f"SELECT title, author, num_pages, size, f_ext FROM books WHERE id = {bookId} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения книги из БД ")

        return (False, False)

    def getBooksAnonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, author FROM books ORDER BY id DESC")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД")
        
        return []