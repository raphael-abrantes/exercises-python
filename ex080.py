aLista = []
for i in range(0,5):
    n = int(input('Digite um número: '))
    if i == 0 or n > aLista[-1]:
        aLista.append(n)
    else:
        c = 0
        while c < len(aLista):
            if n <= aLista[c]:
                aLista.insert(c, n)
                break
            c = c + 1
print(f'\nOs valores digitados em ordem foram {aLista}')
