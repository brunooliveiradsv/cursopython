print('=-'*13)
print('ANALISADOR DE TRIÂNGULOS')
print('=-'*13)

l1 = float(input('Digite o primeito seguimento: '))
l2 = float(input('Digite o segundo seguimento: '))
l3 = float(input('Digite o terceiro seguimento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Forma Triângulo')
    if l1 == l2 == l3:
        print('Equilatero')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não forma um Triangulo')
