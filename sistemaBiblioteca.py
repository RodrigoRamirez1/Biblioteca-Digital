import sqlite3
import cadastro
import consulta

def exibir_menu():
    print("##################################")
    print("BEM VINDO(A) A BIBLIOTECA DIGITAL!")
    print("##################################\n")
    print("1. Adicionar um livro.")
    print("2. Excluir um livro.")
    print("3. Atualizar cadastro do livro.")
    print("4. Buscar livro.")
    print("5. Listar livros:")
    print("6. Sair!\n")

def main():
    biblioteca = sqlite3.connect("biblioteca.db")
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastro.adicionar(biblioteca)
        elif opcao == "2":
            cadastro.excluir()
        elif opcao == "3":
            cadastro.atualizar()
        elif opcao == "4":
            consulta.bucar()
        elif opcao == "5":
            consulta.listar(biblioteca)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()