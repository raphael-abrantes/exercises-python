from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        if '-' not in str(passo):
            passo *= -1
    mostrarpasso = passo
    if '-' in str(passo):
        mostrarpasso = passo * -1
    print('-='*10)
    print(f'Contagem de {inicio} até {fim} de {mostrarpasso} em {mostrarpasso}')
    for c in range(inicio, fim, passo):
        print(c, end=' ', flush=True)
        sleep(0.2)
    print('FIM!')

#inicio
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*10)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
