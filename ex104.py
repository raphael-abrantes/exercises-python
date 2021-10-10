def leiaint(txt:str='Digite um número: '):
    while True:
        n = str(input(txt)).strip()
        if len(n) > 0:
            if n.isnumeric():
                return int(n)
        print('ERRO! Digite um número inteiro válido')


#PROGRAMA
num = leiaint()
print(f'Você digitou o número {num}')
