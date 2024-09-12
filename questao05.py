palavra = str(input("Digite uma palavra: "))
caractere = ""

lista_reversa = []

for i in palavra:
    lista_reversa.insert(0, i)


caractere = ''.join(lista_reversa)

print(caractere)
