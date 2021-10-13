from lib.interface import *

def arqExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArq(arq):
    try:
        a = open(arq, 'wt+')
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {arq} criado com sucesso!')
    finally:
        a.close


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao cadastrar')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao adicionar no arquivo')
        else:
            print(f'Novo registro de {nome}')
    finally:
        a.close
