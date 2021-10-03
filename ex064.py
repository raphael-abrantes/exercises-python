print('Soma de valores. Pressione 999 para finalizar!')
n = int(input('Digite um valor: '))
i = 0
s = 0
while n != 999:
    s = s + n
    n = int(input('Digite um valor: '))
    i = i + 1
print(f'A soma do(s) {i} valores digitados é {s}')
