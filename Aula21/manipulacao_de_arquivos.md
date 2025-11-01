Manipulacao de arquivos:

Arquivo binário é um arquivo compilado para o computador entender.



Permite armazenar, recuperar e processar informações de maneira persistente.



Python oferece diversas.



Modo

"r" Modo de leitura(padrão)

"w" Modo de escrita. Ele vai sobrescrever, caso não exista ele cria.

"a" Modo de adição. Escreve no final do arquivo sem apagá-lo.

"x" Cria um arquivo novo. Retorna erro se já existir.

"b" Modo binário (ex.: Imagens, vídeos, PDFs)

"t" Modo texto

"r+" Leitura e escrita.

"w+" Leitura e escrita. Sobrescreve se já existir, se não existir faz um novo.



open 

leia o arquivo, readline() cria só a primeira linha, readlines() cria uma lista com todas as linhas que tem no arquivo.



Quando a gente colocar um texto a gente faz uma esterilização para fazer um envio pela internet.

Quando a gente recebe e coloca de novo para o formato de string é uma desterilização.



With serve para quando você abrir um arquivo, quando sair do with, ele fecha sozinho.



Context Manager

try:

&nbsp;	with open("arquivo.txt", "a") as f:

&nbsp;		f.write("Nova linha adicionada")

except:

&nbsp;	print("Erro na manipulação do arquivo")





try:

&nbsp;	with open("aula arquivo.txt", "r" as xuxa:

&nbsp;		conteudo = xuxa.read()

&nbsp;	with open("aula\_arquivo\_novo2.txt", "w" as f:

&nbsp;		f.write(conteudo)

except:

&nbsp;	print("")



Manipulação de arquivos binários

* Arquivos binários (imagens, vídeos, PDFs) exigem o uso do modo "b":
* &nbsp;	Lendo um arquivo binário









mideam (site de artigo)

except:

