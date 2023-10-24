def bucar():
    print("Livro buscado")


def listar(database):
    cursor = database.cursor()

    cursor.execute("""SELECT * FROM Livros;""")

    for linha in cursor.fetchall():
        # id = linha[0]
        # nome = linha[1]
        # autor = linha[2]
        # ano = linha[3]
        # genero = linha[4]
        # print("----------------------------")
        # print(nome)
        # print(autor)
        # print(ano)
        # print(genero)
        # print("----------------------------")
        print("----------------------------")
        for celula in linha:
            print(celula)
        print("----------------------------")