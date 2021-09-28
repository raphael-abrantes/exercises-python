num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
option = int(input('Sua opção é: '))
if option == 1:
    print(f'{option} convertido para BINÁRIO é {bin(num)[2:]}')
elif option == 2:
    print(f'{option} convertido para OCTAL é {oct(num)[2:]}')
elif option == 3:
    print(f'{option} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print(f'A opção {option} é inválida')
