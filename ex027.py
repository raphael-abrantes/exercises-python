n = str(input('Entre com um nome completo: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]} e o último nome é {nome[len(nome)-1]}')
