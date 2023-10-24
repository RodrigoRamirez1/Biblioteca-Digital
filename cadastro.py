import sqlite3

def adicionar(database):
    nome = input("\nDigite o Nome do livro: \n").upper()
    autor = input(f"\nDigite o Autor do livro '{nome}': \n").upper()
    ano = int(input(f"\nDigite o Ano de publicação do livro '{nome}': \n"))
    genero = input(f"\nDigite o Gênero do livro '{nome}': \n").upper()
    
    cursor = database.cursor()
    cursor.execute("INSERT INTO Livros VALUES ('"+nome+"', '"+autor+"', "+str(ano)+", '"+genero+"')")
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


def atualizar():
    print("Livro atualizado")
