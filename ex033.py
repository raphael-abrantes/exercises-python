n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
n3 = int(input('Insira o último valor: '))
menor = n1
maior = n1

#Verifica o menor
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

#Verifica o maior
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print (f'O menor valor inserido foi: {menor}')
print (f'O maior valor inserido foi: {maior}')
