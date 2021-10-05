n = [[], []]
vValor = 0
for i in range (1, 8):
    vValor = int(input(f'Digite o {i}° valor: '))
    if vValor % 2 == 0:
        n[0].append(vValor)
    else:
        n[1].append(vValor)
    
n[0].sort()
n[1].sort()
print('-'*50)
print(f'Todos os valores: {n}')
print(f'Os valores pares são: {n[0]}')
print(f'Os valores impares são: {n[1]}')
