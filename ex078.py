aLista = []
vMaior = 0
vMenor = 0
for i in range(0,5):
    aLista.append(int(input(f'Digite um valor para a {i}° posição: ')))
    if i == 0:
        vMaior = vMenor = aLista[i]
    else:
        if aLista[i] > vMaior:
            vMaior = aLista[i]
        if aLista[i] < vMenor:
            vMenor = aLista[i]
print('-'*40)
print(f'A Lista inserida foi: {aLista}')
print('-'*40)
print(f'O maior valor inserido na lista foi: {vMaior}, nas posições: ', end = '')
for i, v in enumerate(aLista):
    if v == vMaior:
        print(f'{i}', end = ' ')
print()
print(f'O menor valor inserido na lista foi: {vMenor}, nas posições: ', end = '')
for i, v in enumerate(aLista):
    if v == vMenor:
        print(f'{i}', end = ' ')
