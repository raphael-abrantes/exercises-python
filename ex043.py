peso = float(input('Qual é seu poso em kg? '))
h = float(input('Qual sua altura em metros? '))
imc = peso / (h ** 2)
print(f'O IMC da pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 < imc <= 25:
    print('Você está no PESO IDEAL!')
elif 25 < imc <= 30:
    print('Você está com SOBREPESO!')
elif 30 < imc <= 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')
