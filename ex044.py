preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
total = preco
if opcao == 1:
    total = preco*0.9
elif opcao == 2:
    total = preco*0.95
elif opcao == 4:
    total = preco*1.2
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} pela forma de pagamento')
