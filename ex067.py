print('Para encerrar, digite um valor negativo')
while True:
    n = int(input('Quer a tabuada de qual valor? '))
    if n < 0:
        print('\nFim do programa!')
        break
    print('-' * 32)
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-' * 32)
