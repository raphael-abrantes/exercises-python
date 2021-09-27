import random

n = int(input('Insita um valor entre 0 e 5: '))
m = random.randint(0,5)
if n == m:
    print('Parabéns, você acertou!')
else:
    print(f'Que pena, você perdeu! O número era {m}')
