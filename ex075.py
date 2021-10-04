c = 0
n = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
print(f'Os valores digitados foram: {n}')
print(f'O número 9 apareceu {n.count(9)} veze(s)')
if 3 in n:
    print(f'O número 3 apareceu pela primeira vez na {n.index(3) + 1}° posição!')
else:
    print('O número 3 não foi inserido na tupla!')

#NúmerosPares
for i in n:
    if i % 2 == 0:
        print('Os número pares são: ', end = '')
        break
    if i % 2 == 1:
        c = c + 1
for i in n:
    if i % 2 == 0:
        print(f'{i}', end = ' ')
if c == 4:
    print('Não foram inseridos números pares!')
