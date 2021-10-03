soma = i = 0
while True:
    num = int(input('Insira um valor [Digite 999 para parar!]: '))
    if num == 999:
        break
    i = i + 1
    soma = soma + num
print(f'A soma dos {i} valores digitados é {soma}')
