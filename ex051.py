n1 = int(input('Insira o primeiro termo de uma PA: '))
r = int(input('Insira a razão da PA: '))
n11 = n1 + (10 * r)
for c in range(n1, n11, r):
    print(f'{c}', end=' → ')
print('Done!')
