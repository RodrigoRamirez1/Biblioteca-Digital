def bucar(database):
    livro = input('Digite o nome do livro a ser buscado: ').upper()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Livros WHERE nome like '%"+livro+"%' ")
    exibir(cursor)
    print("\n>> LIVRO BUSCADO <<\n")


def listar(database):
    cursor = database.cursor()
    cursor.execute("""SELECT id, nome, autor, ano, genero FROM Livros;""")
    exibir(cursor)
    

def exibir(cursor):
    for linha in cursor.fetchall():
        campo = ""
        print("---------------------------------------------------------------------------------------------------")
        for celula in linha:
            campo += str(celula) + "\t"
        print(campo)
    
