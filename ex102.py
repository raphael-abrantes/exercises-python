def fatorial(num, show=False):
    c = num
    equa = str()
    f = 1
    while c > 0:
        equa += f'{c}'
        equa += ' x ' if c > 1 else ' = '
        f *= c
        c -= 1
    equa += str(f)

    if show:
        return equa
    else:
        return f

#PROGRAMA
print(fatorial(5, True))
