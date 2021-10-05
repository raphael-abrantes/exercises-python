aLista = []
aPares = []
aImpares = []

while True:
    n = int(input('Digite um valor: '))
    aLista.append(n)

    #Deseja Continuar?
    vAns = ' '
    while vAns not in 'YySsNn':
        vAns = str(input('Deseja continuar [Y/N]? '))
    if vAns in 'Nn':
        break

for i in range(0, len(aLista)):
    if aLista[i] % 2 == 0:
        aPares.append(aLista[i])
    else:
        aImpares.append(aLista[i])

print(f'A partir da lista {aLista}, gerou-se:')
print(aPares, aImpares)
