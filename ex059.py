n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
option = 0
while option != 5:
    print('''O que deseja fazer com os valores inseridos?
    =-=-=-=-=-=-=-=-=-=-=-=
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa
    =-=-=-=-=-=-=-=-=-=-=-=''')
    option = int(input('Digite a opção desejada: '))
    if option == 1:
        print(f'A soma de {n1} e {n2} é {n1 + n2}')
    elif option == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif option == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif option == 4:
        n1 = int(input('Insira um valor: '))
        n2 = int(input('Insira outro valor: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
