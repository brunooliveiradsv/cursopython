from datetime import date
nasceu = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasceu
if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos e sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'Sua idade é {idade} anos e sua categoria é JUNIOR')
elif idade > 19 and idade <= 25:
    print(f'Sua idade é {idade} anos e sua categoria é SENIOR')