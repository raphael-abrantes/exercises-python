#from math import hypot
catO = float(input('Insira o valor do Cateto Oposto: '))
catA = float(input('Insira o valor do Cateto Adjacente: '))
hip = (catO ** 2 + catA ** 2) ** (1 / 2)
#hip = hypot(catO,catA)
print (f'A hipotenusa de {catO} e {catA} é igual {hip}')
