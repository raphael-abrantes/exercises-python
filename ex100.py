from random import randint

def sorteia(lis):
    for n in range(0, 5):
        lis.append(randint(1, 10))
    print(f'Os valores sorteados foram {lis}')

def somapares(lis):
    soma = 0
    for n in lis:
        if n % 2 == 0:
            soma += n
    print('-='*25)
    print(f'A soma dos valores pares de {lis} é igual a = {soma}')


numeros = list()

sorteia(numeros)
somapares(numeros)
