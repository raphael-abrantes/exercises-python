from random import randint
print('PEDRA | PAPEL | TESOURA')
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('-=' * 11)
print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-=' * 11)
jogador = int(input('Qual é a sua jogada? '))
pcPlay = itens[computador]
playerPlay = itens[jogador]
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Computador VENCEU')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA!')
else:
    print('Jogada INVÁLIDA!')
print('=-' * 29)
print(f'O jogador escolheu {playerPlay} e o computador escolheu {pcPlay}')
print('=-' * 29)
