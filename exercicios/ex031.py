distance = float(input('Qual a distancia da viagem em km? '))
if distance <= 200:
    cobrar = distance * 0.50
else:
    cobrar = distance * 0.45
print(f'O valor da passagem será de R${cobrar:.2f}')