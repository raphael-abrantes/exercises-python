aMatriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range (0, 3):
        aMatriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-'*32)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{aMatriz[i][j]:^7}]', end='')
    print()
