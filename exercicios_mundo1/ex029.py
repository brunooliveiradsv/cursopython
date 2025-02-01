vel = float(input('Qual a velocidade em Km/h? '))
multa = (vel - 80) * 7
if vel  > 120:
    print('Você é louco, quer se matar?')
    print(f'Valor R${multa}')
elif vel > 80:
    print(f'Você está acima de  80km/h e acabou de ser multado.')
    print(f'Valor R${multa}')
else:
    print(f'Muito bem, você segue as normas de trânsito!')
