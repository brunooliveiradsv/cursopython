import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print(f'O comprimento da hipotenusa será {math.hypot(co, ca):.2f}')