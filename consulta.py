def bucar():
    print("Livro buscado")


def listar(database):
    cursor = database.cursor()

    cursor.execute("""SELECT * FROM Livros;""")

    for linha in cursor.fetchall():
        print(linha)
    database.close()
print("Livros listados")