sexo = str(input('Infome o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Informação errada!')
    sexo = str(input('Infome o seu sexo [M/F]: ')).strip().upper()[0]
print(f'O sexo informado é {sexo}')
