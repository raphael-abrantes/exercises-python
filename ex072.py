tNumeros0a20 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    vValor = int(input('Insira um valor entre 0 e 20: '))
    if 0 <= vValor <= 20:
        break
    print(f'O valor {vValor} não está em um intervalo de 0 a 20. Respeite o comando!\n')
print(f'O valor {vValor} por extenso é: {tNumeros0a20[vValor]}')
