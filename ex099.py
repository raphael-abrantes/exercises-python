def maior(*num):
    print('-='*20)
    print('Analisando...')
    maior = 0
    for n in num:
        if n > maior:
            maior = n
        print(n, end=' ')
    print(f'Foram informados {len(num)} números ao total.')
    print(f'O maior valor informado foi {maior}.')


#inicio
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
