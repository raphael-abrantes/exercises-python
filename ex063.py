print('-'*37)
print('Sequência de fibonacci'.center(37))
print('-'*37 + '\n')
print('~'*37)
n = int(input('Quantos termos deseja visualizar? '))
print('~'*37)
t1 = 0
t2 = 1
t3 = 0
i = 3
print(f'{t1} → {t2} → ', end='')
while i <= n:
    t3 = t1 + t2
    print (f'{t3} → ' if i != n else f'{t3}', end='')
    i = i + 1
    t1 = t2
    t2 = t3
print('\n\nFim')
