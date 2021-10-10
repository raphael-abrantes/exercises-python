def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or  entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(txt:str='Digite um número: '):
    while True:
        n = str(input(txt)).strip()
        if len(n) > 0:
            if n.isnumeric():
                return int(n)
        print('ERRO! Digite um número inteiro válido')

