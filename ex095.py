jogador = dict()
golList = list()
cadastro = list()

while True:
    print('°~~'*15)
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    print('°~~'*15)
    for g in range(0, partidas):
        golList.append(int(input(f'Quantos gols na partida {g+1}? ')))
    jogador['total'] = sum(golList)
    
    jogador['gols'] = golList[:]
    golList.clear()
    cadastro.append(jogador.copy())

    resposta = ' '
    while resposta not in 'SN':
        print('-=-'*10)
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break

print('°~~'*20)
print(f'{"cod":<} {"Nome":<15} {"Gols":<20} {"Total":<5}')
print('-'*50)
for i, reg in enumerate(cadastro):
    print(f'{i:>3} {reg["nome"]:<15} {str(reg["gols"]):<20} {reg["total"]:<5}')

while True:
    print('°~~'*20)
    cod = int(input('Escolha um jogador para detalhes: '))
    while  (cod >= len(cadastro) or cod < 0) and cod != 999:
        print('°~~'*20)
        print('Código incorreto! Tente novamente')
        cod = int(input('Escolha um jogador para detalhes: '))
    if cod == 999:
        break
    detalhe = cadastro[cod]
    print('°~~'*20)
    print(f'-==Levantamento do jogador {detalhe["nome"].upper()}==-')
    for i, g in enumerate(detalhe['gols']):
        print(f'No jogo {i+1} fez {g} gols.')
print('-=-'*15)
print('>FIM DO PROGRAMA<')
