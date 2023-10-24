import sqlite3

def adicionar(database):
    nome = input("\nDigite o Nome do livro: \n").upper()
    autor = input(f"\nDigite o Autor do livro '{nome}': \n").upper()
    ano = int(input(f"\nDigite o Ano de publicação do livro '{nome}': \n"))
    genero = input(f"\nDigite o Gênero do livro '{nome}': \n").upper()
    
    cursor = database.cursor()
    cursor.execute("INSERT INTO Livros (nome, autor, ano, genero) VALUES ('"+nome+"', '"+autor+"', "+str(ano)+", '"+genero+"')")
    database.commit()
    print("\n>> LIVRO CADASTRADO COM SUCESSO! <<\n")



def excluir(database):
    try:
        nome = input("\n Digite o Nome do livro que será deletado: \n").upper()

        cursor = database.cursor()
        cursor.execute("DELETE FROM Livros WHERE nome = '"+nome+"'")
        database.commit()
        print("\n>> LIVRO EXCLUÍDO <<\n")

    except sqlite3.Error as erro:
        print(f"\n>> ERRO AO EXCLUIR: {erro} <<\n")




def atualizar(database):
    identificador = input("Digite o ID do Livro a ser atualizado: ")
    campos = ('nome', 'autor', 'ano', 'genero')
    valores = ()

    print("Preencha os campos que você quer atualizar, (Deixe vazio caso não queria alterar)")

    for campo in campos:
        valores += (input(campo + ':').upper(),)

    sql = "UPDATE Livros SET "

    for indice, campo in enumerate(campos):
        if valores[indice] != '':
            sql += campo + "= '" + valores[indice] + "',"

    sql = sql [0:len(sql)-1]
    sql += " WHERE id = " + identificador

    print(sql)

    cursor = database.cursor()
    cursor.execute(sql)
    database.commit()
    print("\n>> LIVROS ATUALIZADOS <<\n")
