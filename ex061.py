n1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Qual a razão da PA? '))
nx = n1
i = 1
while i <= 10:
    print(f'{nx} → ' if i != 10 else f'{nx}', end='')
    nx = nx + r
    i = i + 1
