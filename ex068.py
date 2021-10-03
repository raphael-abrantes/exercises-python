from random import randint

i = 0
while True:
    n = int(input('Digite um valor: '))
    comp = randint(0,9)
    tot = n + comp
    PouI = ' '
    while PouI not in 'PpIi':
        PouI = str(input('Par ou ímpar [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {n} e o computador jogou {comp}. Portanto, o total é {tot}')
    if PouI == 'P':
        if tot % 2 == 0:
            print('Deu par! Você venceu!\n')
            i = i + 1
        else:
            print('Deu ímpar, você perdeu!\n')
            break
    if PouI == 'I':
        if tot % 2 != 0:
            print('Deu ímpar! Você venceu!\n')
            i = i + 1
        else: 
            print('Deu par, você perdeu!\n')
            break
print(f'Você venceu {i} vez(es)')
print('Fim do programa!')
