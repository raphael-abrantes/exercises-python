from random import randint
from time import sleep
megasena = list()
jogo = list()

print('-='*15)
print(f'{"MEGA SENA":^30}')
print('-='*15)
njogos = int(input('Quantos jogos você quer sortear? '))

print(f'==== SORTEANDO OS {njogos} JOGOS ====')
for j in range(0, njogos):
    sleep(0.5)
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    megasena.append(jogo[:])
    jogo.clear()
    print(f'Jogo {j+1}: {megasena[j]}')
print('-='*15)
print(f'{"BOA SORTE":^30}')
print('-='*15)
