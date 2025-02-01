import random

a1 = str(input('Primeiro nome: '))
a2 = str(input('Segundo nome: '))
a3 = str(input('Terceiro nome: '))
a4 = str(input('Quarto nome: '))
a5 = str(input('Quinto nome: '))
a6 = str(input('Sexto nome: '))
lista = [a1, a2, a3, a4, a5, a6]
escolhido = random.choice(lista)
print(escolhido)