valorCasa = float(input('Digite o valor da casa: R$'))
salario =  float(input('Digite o salário: R$'))
anos = float(input('Quantos anos irá pagar? '))
prestacao = valorCasa / (anos * 12)
if prestacao <= (salario * 0.3):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
