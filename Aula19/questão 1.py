from modulo import *
# pedir o nome do livro e as N avalisções vão ser separadas por , 10, 8, 10, vão pegar a string e colocar em uma tupla. Usa split por vírgula.
while True:
    print("=" * 27)
    try:
        menu = int(input("Digite uma opção: \n1. Cadastrar livros. \n2. Calcular a média das avaliações. \n3. Buscar um livro pelo título. \n4. Exibir todos os livros cadastrados. \n5. Sair.  \n"))
    except:
        print("Digite só números. Ex: 1")
        continue
    print("=" * 27)
    match menu:
        case 1:
            titulo_livro = input("Digite o título do livro: ").strip()
            ok = verificador_digitou_alguma_coisa(titulo_livro)
            if not ok[0]:
                print(ok[1])
                continue

            autor_livro = input("Digite o nome do autor: ").strip()
            ok = verificador_digitou_alguma_coisa(autor_livro)
            if not ok[0]:
                print(ok[1])
                continue

            ano_livro = input("Digite o ano de publicação do livro: ")
            ok = verificador_ano(ano_livro)
            if not ok[0]:
                print(ok[1])
                continue

            while True:
                avaliacao_livro = input("Digite as avaliações do livro: ") 
                avaliacoes = avaliacao_livro.split(",")
            
                ok = verificador_avaliacao(avaliacoes)
                if not ok[0]:
                    print(ok[1])
                    continue
                else:
                    break
            notas = tupla_avaliacoes(avaliacoes)

            if ok:
                print(cadastrar_livro(titulo_livro, autor_livro, ano_livro, notas))
            else:
                print("Erro: Livro não cadastrado.")
        case 2:
            if lista:
                titulo = " ".join(input("Digite o nome do livro: ").split(" ")).strip() # Era para ter deixado o split vazio
                media = calcular_media(titulo.lower())
                if media:
                    print(media)
                else:
                    print("Erro: Livro não encontrada.")
            else:
                print("Erro: Lista vazia.")
        case 3:
            if lista:
                titulo = " ".join(input("Digite o nome do livro: ").split(" ")).strip()
                buscou = buscar_livro(titulo.lower())
                if buscou:
                    print(buscou)
                else:
                    print("Erro: Livro não encontrado.")
            else:
                print("Erro: Lista vazia")
        case 4:
            if lista:
                for livro in lista:
                    print(livro)
            else:
                print("Lista vazia.")
        case 5:
            print("Programa encerrado.")
            break
        case _:
            print("Erro: Digite um número dentro das opções. Exemplo: 2")