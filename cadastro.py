def adicionar(database):
    nome = input("\nDigite o Nome do livro: \n")
    autor = input(f"\nDigite o Autor do livro '{nome}': \n")
    ano = int(input(f"\nDigite o Ano de publicação do livro '{nome}': \n"))
    genero = input(f"\nDigite o Gênero do livro '{nome}': \n")
    
    cursor = database.cursor()
    cursor.execute("INSERT INTO Livros VALUES ('"+nome+"', '"+autor+"', "+str(ano)+", '"+genero+"')")
    database.commit()
    print("\nLIVRO CADASTRADO COM SUCESSO! \n")

def excluir():

    
    print("Livro excluido")


def atualizar():
    print("Livro atualizado")
