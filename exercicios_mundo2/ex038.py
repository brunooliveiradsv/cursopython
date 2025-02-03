n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha mais um número: '))

if n1 > n2:
    print(f'O Primeiro número é maior que o segundo.')
elif n1 < n2:
    print(f'Segundo número é maior que o primeiro.')
else:
    print('Não existe número maior, os dois são iguais.')
