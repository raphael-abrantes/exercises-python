import sys, os
caminho = os.path.dirname(__file__)
sys.path.append(caminho[:caminho.find('exs')])
from time import sleep

def printlin(txt):
    print(f'~'*int(len(txt) + 4),flush=False)
    print(f'  {txt}  ',flush=False)
    print(f'~'*int(len(txt) + 4), flush=False)

def pyhelp():
    while True:
        printlin('SISTEMA DE AJUDA PyHELP')
        pesquisa = str(input('Função ou Biblioteca > ')).strip().lower()
        if pesquisa.upper() == 'END':
            break
        printlin(f'Acessando o Manual de "{pesquisa}"')
        sleep(1)
        print(f'{help(pesquisa)}')
        sleep(2)
    printlin(f'ATÉ LOGO')

#PROGRAMA
pyhelp()
