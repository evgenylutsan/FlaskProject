from PyPDF2 import PdfFileReader
import os
import fitz
from pathlib import Path
import sqlite3
from psycopg2 import connect
from pathlib import Path

name = input("Введите название файла: ") 

# if os.path.exists(path_pdf = "C:\\Users\\lutsa\\OneDrive\\Рабочий стол\\python_project\\books\\" + name + ".pdf") == False:
#     print("Данный файл отсутствует в директории")

path_pdf = "C:\\Users\\lutsa\\OneDrive\\Рабочий стол\\python_project\\books\\" + name + ".pdf"

pdf_path = path_pdf
#     Path.home()
#     / "C:\\Users\\lutsa\\OneDrive\\Рабочий стол\\python_project\\books\\" + name + ".pdf"
# )

pdf = PdfFileReader(str(pdf_path))
t = os.path.basename(pdf_path)
title = os.path.splitext(t.rpartition('_')[-1])[0]
author = os.path.splitext(t.rpartition('_')[0])[0]
f = os.stat(pdf_path)

def pretty_size(size):
    s = ['Б', 'КБ', 'МБ']
    i = 0
    while size > 1023 and i < 3:
        size = round(size/1024)
        i += 1
    return f'{size} {s[i]}'

size = f.st_size
hsize = pretty_size(size)

count_page = pdf.getNumPages()
ext = os.path.splitext(t)[1]

doc = fitz.open(pdf_path)
page = doc.load_page(0)
pix = page.get_pixmap()
output = "C:\\Users\lutsa\\OneDrive\\Рабочий стол\\python_project\\static\\img\\prewiew - " + title + ".png"
pix.save(output)

path_pic = output

def pict_binary(pic_path):
    f = open(pic_path, 'rb')
    pic_bin = f.read()
    return pic_bin
bin_pic = pict_binary(pic_path = path_pic)

print(f"Название книги: {title}")
print(f"Автор книги: {author}")
print(f"Путь файла: {pdf_path}")
print(f"Кол-во страниц: {count_page}")
print(f"Размер файла: {hsize}")
print(f"Расширение файла: {ext}")


db = sqlite3.connect('books.db')
cur = db.cursor()

data = [
    (title, author, count_page, hsize, ext, bin_pic)
]

cur.executemany("insert into books values (Null, ?, ?, ?, ?, ?, ?);", data)
db.commit()

p = Path("books.db").resolve()

print("Расположение базы данных: ", p)