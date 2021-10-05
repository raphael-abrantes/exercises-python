aLista = []
while True:
    n = int(input('Digite um valor: '))
    aLista.append(n)

    #Deseja Continuar?
    vAns = ' '
    while vAns not in 'YySsNn':
        vAns = str(input('Deseja continuar [Y/N]? '))
    if vAns in 'Nn':
        break
print(f'Foram digitados {len(aLista)} valores na lista')
aLista.sort(reverse=True)
print(f'A ordem decrescente é {aLista}')

if 5 in aLista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
