from datetime import date

nasceu = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasceu
if idade < 18:
    print(f'Você está com {idade} anos de idade e ainda vai se alistar.')
elif idade == 18:
    print('Voce tem 18 anos e deve ir se alistar!')
elif idade > 18:
    print(f'Você tem {idade} anos e já deve ter se alistado a {idade - 18} anos.')
