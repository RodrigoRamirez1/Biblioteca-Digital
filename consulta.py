def bucar():
    print("Livro buscado")


def listar(database):
    cursor = database.cursor()

    cursor.execute("""SELECT * FROM Livros;""")

    for linha in cursor.fetchall():
        nome = linha[0]
        autor = linha[1]
        ano = linha[2]
        genero = linha[3]
        print("----------------------------")
        print(nome)
        print(autor)
        print(ano)
        print(genero)
        print("----------------------------")
