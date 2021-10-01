frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
nospace = ''.join(palavras)
inverso = nospace[::-1]
print(f'O inverso de {nospace} é {inverso}')
if inverso == nospace:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

###Outra forma, mais convencional é:
#inverso = ''
#for l in range (len(nospace) - 1,-1,-1):
#    inverso = inverso + nospace[l]