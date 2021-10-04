aLista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in aLista:
        aLista.append(n)
        print('Valor adicionado com sucesso!\n')
    else:
        print('Valor duplicado. Não foi adicionado à lista!\n')

    vAns = ' '
    while vAns not in 'YySsNn':
        vAns = str(input('Deseja continuar [Y/N]? '))
    if vAns in 'Nn':
        break   

aLista.sort()
print(f'\nOs valoes inseridos em ordem foram {aLista}\n')
