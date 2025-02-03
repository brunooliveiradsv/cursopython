import random
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']

computador = random.randint(0,2)

jogador = int(input('''[0] Pedra
[1] Papel  
[2] Tesoura
Qual a sua jogada? '''))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(1)

print('=-'*20)
print(f'O jogador escolheu {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
print('=-'*20)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
else:
    print('JOGADA INVALIDA')