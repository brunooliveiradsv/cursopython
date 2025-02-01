print('=-'*12)
print('Analisador de Triangulos')
print('=-'*12)
seg1 = float(input('Digite o primeito seguimento: '))
seg2 = float(input('Digite o segundo seguimento: '))
seg3 = float(input('Digite o terceiro seguimento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')