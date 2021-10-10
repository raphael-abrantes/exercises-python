from utilsPy.utilspackage import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é: {moeda.metade(p, True)}')
print(f'O dobro de {p} é: {moeda.dobro(p, True)}')
print(f'Com um aumento de 10% o valor fica: {moeda.aumentar(p, 10, True)}')
print(f'Com uma redução de 5% o valor fica: {moeda.diminuir(p, 5, True)}')
