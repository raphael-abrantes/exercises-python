jogador = {'nome':'', 'gols':list(), 'total':0}
bolasdentro = list()

jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
print('~°'*25)
for g in range(0, partidas):
    bolasdentro.append(int(input(f'Quantos gols na partida {g+1}? ')))
jogador['total'] = sum(bolasdentro)
jogador['gols'] = bolasdentro[:]
bolasdentro.clear()
print('~°'*30)
print(jogador)
print('~°'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('~°'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'{"=>":>4} Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
