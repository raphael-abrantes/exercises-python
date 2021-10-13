def leiaInt(txt:str='Digite um número inteiro: '):
    while True:
        try:
            n = int(input(txt).replace(',','.').strip())
        except KeyboardInterrupt:
            print('\nO usuário não entrou com nenhum valor!')
            return int(0)
        except:
            print('\033[031mERRO: digite um número inteiro válido!\033[m')
            continue
        else:
            return int(n)
            

def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc