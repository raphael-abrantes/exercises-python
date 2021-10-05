aMatriz = [[0, 0 , 0], [0, 0 , 0], [0, 0 , 0]]
vSomaPares = 0
vSomaColuna3 = 0
vMaiorLinha2 = 0
for i in range(0, 3):
    for j in range(0, 3):
        aMatriz[i][j] = int(input(f'Insira um valor para [{i}, {j}]: '))
print('-'*32)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{aMatriz[i][j]:^7}]', end='')
        if aMatriz[i][j] % 2 == 0:
            vSomaPares = vSomaPares + aMatriz[i][j]
    print()
for i in range(0, 3):
    vSomaColuna3 = vSomaColuna3 + aMatriz[i][2]
for j in range(0, 3):
    if j == 0:
        vMaiorLinha2 = aMatriz[1][j]
    else:
        if aMatriz[1][j] > vMaiorLinha2:
            vMaiorLinha2 = aMatriz[1][j]
print('-'*32)
print(f'A soma dos valores pares é {vSomaPares}')
print(f'A soma dos valores na terceira coluna é {vSomaColuna3}')
print(f'O maior valor da segunda linha é {vMaiorLinha2}')
