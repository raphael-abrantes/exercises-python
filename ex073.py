tListaBrasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('-'*35)
print(f'Lista dos times do Brasileirão 20/11/2018: {tListaBrasileirao}')
print('-'*35)
print(f'Os 5 primeiros colocados eram: {tListaBrasileirao[0:5]}')
print('-'*35)
print(f'Os 4 últimos colocados eram: {tListaBrasileirao[-4:]}')
print('-'*35)
print(f'A lista em ordem alfabética é: {sorted(tListaBrasileirao)}')
print('-'*35)
print(f'A Chapecoense está na {tListaBrasileirao.index("Chapecoense") + 1}° posição')
print('-'*35)
