n1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Qual a razão da PA? '))
x = int(input('Quantos termos da PA deseja visualizar? '))
nx = n1
i = 1
while x != 0:
    while i <= x:
        print(f'{nx} → ' if i != x else f'{nx}', end='')
        nx = nx + r
        i = i + 1
    print('\n')
    x = int(input('Quantos termos da PA deseja visualizar? '))
    i = 1
    nx = n1
