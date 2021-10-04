tPalavras = (
    'aprender',
    'programar',
    'linguagem',
    'python',
    'curso',
    'gratis',
    'try'
)

for i in tPalavras:
    print(f'\nNa palavra {i.upper()} temos: ', end = '')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
