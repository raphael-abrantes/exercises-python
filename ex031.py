km = float(input('Digite a distância do destino: '))
if km <= 200:
    print(f'O valor da passagem é de {km*0.5:.2f}')
else:
    print(f'O valor da passagem é de {km*0.45:.2f}')
