def voto(nasc = int()):
    from datetime import datetime
    i = datetime.now().year - nasc
    if i >= 65 or (i >= 16 and i < 18):
        return f'Com {i} anos. O voto é OPCIONAL!'
    elif i < 16:
        return f'Com {i} anos. O voto é NEGADO!'
    else:
        return f'Com {i} anos. O voto é OBRIGATÓRIO!'


#PROGRAMA
idade = int(input('Digite o ano de nascimento: '))
print(voto(idade))
