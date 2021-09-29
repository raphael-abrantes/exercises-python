print('Entre com seis valores. A saída será a soma dos pares')
soma = 0
n = 0
s = 0
for c in range(1,7):
    n = int(input(f'Insira o valor {c}° valor: '))
    if n % 2 == 0:
        s = s + n
print(f'A soma entre os valores pares são {s}')
