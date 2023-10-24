import sqlite3

biblioteca = sqlite3.connect('biblioteca.db')

cursor = biblioteca.cursor()

cursor.execute("CREATE TABLE Livros(nome text, autor text, ano integer, genero text)")
