def ficha(nome:str='<desconhecido>', numg=0):
    n = nome
    g = numg
    if len(n.strip()) <= 0:
        n = '<desconhecido>'
    if len(g.strip()) <= 0:
        g = 0

    return f'O jogador {n}, fez {g} gol(s) no campeonato.'


#PROGRAMA
nome = str(input('Nome do jogador: '))
numgols = input('Número de gols: ')
print(ficha(nome, numgols))
