from datetime import date
today = date.today().year
tMaior = 0
for i in range(1, 8):
    nasc = int(input(f'Em que ano a {i}° nasceu? '))
    idade = today - nasc
    if idade >= 21:
        tMaior = tMaior + 1
print(f'Existem {tMaior} pessoas na maioridade.')
print(f'Existem {7 - tMaior} pessoas na menoridade.')
