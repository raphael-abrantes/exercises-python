velocidade = float(input('Insira a velocidade do carro em km/h: '))
vmax = 80
if velocidade > vmax:
    multa = (velocidade - vmax) * 7
    print(f'Você foi multado! Velocidade acima da permitida ({vmax}km/h)')
    print(f'A multa será de R${multa:.2f}')
else:
    print('Tudo correto, tenha um bom dia!')
