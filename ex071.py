print('-'*35)
print('Simulador de ATM'.center(35,' '))
print('-'*35)
#Cédulas disponíveis : 50, 20, 10 e 1
vValorSacado = int(input('Qual valor deseja sacar? '))
print('-'*35)
vTotal = vValorSacado
vNota = 50
count = 0
while True:
    if vTotal >= vNota:
        vTotal = vTotal - vNota
        count = count + 1
    else:
        if count > 0:
            print(f'Total de {count} cédula(s) de {vNota}!')
        if vNota == 50:
            vNota = 20
        elif vNota == 20:
            vNota = 10
        elif vNota == 10:
            vNota = 1
        count = 0
        if vTotal == 0:
            break
