def notas(*n, sit:bool=False):
    cont = maior = menor = totnota = 0
    aluno = dict()
    if len(n) <= 0:
        return 'Não foi informado nenhuma nota!'
    while cont < len(n):
        notaatual = n[cont]
        if cont == 0:
            maior = notaatual
            menor = notaatual
        else:
            if notaatual > maior:
                maior = notaatual
            if notaatual < menor:
                menor = notaatual
        totnota += notaatual
        cont += 1
    media = totnota/cont
    aluno['total'] = cont
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['media'] = media
    if sit:
        if media < 7 and media > 5:
            aluno['situacao'] = 'RAZOÁVEL'
        elif media <= 5:
            aluno['situacao'] = 'RUIM'
        else:
            aluno['situacao'] = 'BOA'
    return aluno


#PROGRAMA
print(notas(5.5, 2.5, 10, 6.5, sit=True))
