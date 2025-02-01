salario = float(input('Qual o salário do funcionario? '))
if salario >= 1250:
    aumento = salario + (salario * 10/100)
    print(f'Quem ganhava {salario} passa a ganhar R${aumento:.2f}')
else:
    aumento = salario + (salario * 15/100)
    print(f'Quem ganhava {salario} passa a ganhar R${aumento:.2f}')