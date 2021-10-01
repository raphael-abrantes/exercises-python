from random import randint

n = -1
m = randint(0,10)
tries = 0
while not n == m:
    n = int(input('Insita um valor entre 0 e 10: '))  
    tries = tries + 1
    if not n==m:
        if n < m:
            print('Mais... Tente novamente:')
        else:
            print('Menos... Tente novamente')
print(f'Parabéns, você acertou com {tries} tentativa(s)!')
