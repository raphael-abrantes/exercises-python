frase = str(input('Digite qualquer frase: ')).upper().strip()
print('A frase possui {} letras A'.format(frase.count('A')))
print('A letra A aparece na posição {} pela primeira vez'.format(frase.find('A')+1))
print('A letra A aparece na posição {} pela última vez'.format(frase.rfind('A')+1))
