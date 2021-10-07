from random import randint
from time import sleep
from operator import itemgetter #usando pra pegar uma parte do dicionario 0 = chave / 1 = valor

jogo = dict()
rank = list()
cont = 0

while True:
    num = randint(1,6)
    if num not in jogo.values():
        cont += 1
        jogo[f'jogador{cont}'] = num
    if cont == 4:
        break

for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
print('~*+'*10)
print('     -====RANKING====-')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, r in enumerate(rank):
    print(f'Em {i+1}º lugar, {r[0]} com {r[1]}')
    sleep(0.5)
