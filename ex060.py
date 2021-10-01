#Cálculo de Fatorial
n = int(input('Insira o valor desejado: '))
i = n
f = 1
while n < 0:
    n = int(input('Valor inválido. Por favor, insira um valor maior ou igual a zero: '))
print(f'Calculando {n}! = ', end='')
while i > 0:
    print(f'{i}', end='')
    print(f' x ' if i > 1 else ' = ', end='')
    f = f * i
    i = i - 1
print(f'{f}')
