lista = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Transferidor', 4.20, 
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90,
)

print('-'*39)
print('LISTA DE PREÇO'.center(39,' '))
print('-'*39)
for n in range(0,len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]}'.ljust(30,'.'), end = '')
    else:
        print(f'R$', end = '')
        print(f'{lista[n]:.2f}'.rjust(7,' '))
print('-'*39)
