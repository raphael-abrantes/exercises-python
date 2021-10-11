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


def leiaFloat(txt:str='Digite um número real: '):
    while True:
        try:
            n = float(input(txt).replace(',','.').strip())
        except KeyboardInterrupt:
            print('\nO usuário não entrou com nenhum valor!')
            return float(0)
        except:
            print('\033[031mERRO: digite um número real válido!\033[m')
            continue
        else:
            return float(n)


inteiro = leiaInt()
real = leiaFloat()
print(f'O valor inteiro digitado foi {inteiro} e o número real foi {real}')
