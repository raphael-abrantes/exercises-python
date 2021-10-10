from utilsPy.utilspackage import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é: R${moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é: R${moeda.dobro(p)}')
print(f'Com um aumento de 10% o valor fica: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Com uma redução de 5% o valor fica: {moeda.moeda(moeda.diminuir(p, 5))}')
