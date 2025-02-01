"""tempo = int(input('Quantos anos tem seu carro? '))

if tempo <=3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')"""
import random

num = (random.randint(1, 5))
acerto = int(input('Escolha um número de 0 a 5: '))
if acerto == num:
    print('Parabéns você acertou!')
else:
    print('Você errou.')
print(f'O numero sorteado foi {num}')