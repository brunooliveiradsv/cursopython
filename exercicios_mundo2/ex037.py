num = int(input('Escolha um número inteiro: '))
escolha = int(input('Qual será a base de conversão\nDigite 1 para Binário\nDigite 2 para octal\nDigite 3 para Hexadecimal '))
if escolha == 1:
    num = bin(num)[2:]
    print('Binário: {}'.format(num))
elif escolha == 2:
    num = oct(num)[2:]
    print('Octal: {}'.format(num))
elif escolha == 3:
    num = hex(num)[2:]
    print('Hexadecimal: {}'.format(num))
else:
    print('Opção invalida')