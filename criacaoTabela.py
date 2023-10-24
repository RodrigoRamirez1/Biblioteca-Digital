import sqlite3

biblioteca = sqlite3.connect('biblioteca.db')

cursor = biblioteca.cursor()

cursor.execute("CREATE TABLE Livros(id integer primary key autoincrement, nome text, autor text, ano integer, genero text)")
