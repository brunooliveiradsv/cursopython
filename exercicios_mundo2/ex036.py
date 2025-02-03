valorCasa = float(input('Qual o valor da casa que você deseja comprar? R$'))
salario = float(input('Quanto você recebe? R$'))
prazo = int(input('Em quantos anos deseja pagar? '))
prestacao = valorCasa / (prazo * 12)
minimo = salario * 30 / 100

if prestacao >= minimo:
    print('Não foi possível realizar seu Empréstimo.')
else:
    print('Parabéns, seu emprestimo foi aprovado!')