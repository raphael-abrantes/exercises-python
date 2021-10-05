vExpressao = str(input('Digite uma expressão: '))
aLista = []
for l in vExpressao:
    if l == '(':
        aLista.append(l)
    elif l == ')':
        if len(aLista) > 0:
            aLista.pop()
        else:
            aLista.append(l)
            break

if len(aLista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
