n1 = int(input('Insira um lado do triângulo: '))
n2 = int(input('Insira outro lado do triângulo: '))
n3 = int(input('Insira o último lado do triângulo: '))
if n1 + n2 < n3 and n1 + n3 < n2 and n2 + n3 < n1:
    print('Os lados formam um triângulo!')
else:
    print('Os lados NÃO formam um triângulo!')
