num = int(input('Escolha um número: '))
print('=-'*15)
print(f'ESSA É A TABUADA DO {num}:')
print('=-'*15)
for tabuada in range(1, 11):
    print(f'{num} x {tabuada} = {num * tabuada}')
print('=-'*15)