vTotal = 0
i = 0
vMenorValor = 0
cont = 1
vMenorValorItem = ''

while True:
    vItem = str(input('Insira o nome do produto: '))
    vValor = float(input('Valor do produto: R$'))
    vTotal = vTotal + vValor
    if vValor >= 1000:
        i = i + 1
    if cont == 1:
        vMenorValor = vValor
        vMenorValorItem = vItem
    else:
        if vValor < vMenorValor:
            vMenorValor = vValor
            vMenorValorItem = vItem
    cont = cont + 1

    vAns = ' '
    while vAns not in 'YyNnSs':
        vAns = str(input('Deseja continuar [Y/N]? '))
    if vAns in 'Nn':
        break
    print('-'*40)
#print('{:-^40}'.format('Fim do Programa'))
print('Fim do Programa'.center(40,'-'))
print(f'Temos {i} produto(s) custando mais que R$1000.00')
print(f'O produto mais barato foi o {vMenorValorItem} custando R${vMenorValor:.2f}')
