aTemp = []
aLista = []
vMaior = vMenor = 0

while True:
    aTemp.append(str(input('Nome: ')))
    aTemp.append(float(input('Peso: ')))

    if len(aLista) == 0:
        vMaior = vMenor = aTemp[1]
    else:
        if aTemp[1] > vMaior:
            vMaior = aTemp[1]
        if aTemp[1] < vMenor:
            vMenor = aTemp[1]

    aLista.append(aTemp[:])
    aTemp.clear()
    vAns = ' '
    while vAns not in 'YySsNn':
        vAns = str(input('Deseja continuar [Y/N]? ')).upper().strip()
    if vAns in 'Nn':
        break
print('-'*50)
print(f'Ao todo, foram cadastradas {len(aLista)} pessoas.')
print(f'O maior peso foi de {vMaior}kg, de ', end='')
for p in aLista:
    if p[1] == vMaior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {vMenor}kg, de ', end='')
for p in aLista:
    if p[1] == vMenor:
        print(f'[{p[0]}] ',end='')
