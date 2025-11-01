idade = int(input("Qual é a idade? "))
tempo_contribuição = int(input("Qual é seu tempo de contribuição como trabalhador? "))

idade = idade >= 60
tempo_contribuição = tempo_contribuição >= 25

aposentavel = idade and tempo_contribuição
print(f"Aposentável: {aposentavel}")
