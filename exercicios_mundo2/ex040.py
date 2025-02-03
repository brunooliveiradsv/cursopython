from traceback import print_tb

n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média foi {media} e foi REPROVADO')
elif media >= 5 and media < 7:
    print(f'Sua média foi {media} e ficou de RECUPERAÇÃO')
else:
    print(f'Sua média foi {media} e foi APROVADO')