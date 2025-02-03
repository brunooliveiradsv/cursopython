produto = float(input('Digite o valor do produto R$'))
dinheiroCheque = produto - (produto * 10 / 100)
avistaCartao = produto - (produto * 5 / 100)
duasxCartao = produto
maisxCartao = produto + (produto * 20 / 100)

fp = int(input('1-Dinheiro/Cheque\n2-A vista no Cartão\n3-2x no Cartão\n4-Até 12x no Cartão\n Escolha a forma de pagamento: '))

if fp == 1:
    print('No dinheiro ou cheque à 10% de desconto R${:.2f}'.format(dinheiroCheque))
elif fp == 2:
    print('A vista no cartão à 5% de desconto R${:.2f}'.format(avistaCartao))
elif fp == 3:
    print('Em 2x no Cartão não à descontos R${:.2f}'.format(duasxCartao))
elif fp == 4:
    totalparc = int(('Quantas parcelas? '))
    print(f'Você parcelou em {totalparc}x de {produto / totalparc} R${maisxCartao:.2f}')