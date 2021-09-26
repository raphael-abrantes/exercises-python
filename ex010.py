reais = float(input('Quantos reais você tem na carteira? R$'))
cotacaoRSDUSD = float(input('Qual a cotação atual do dólar para real? R$'))
dolares = reais / cotacaoRSDUSD
print(f'Com \033[32mR${reais:.2f}\033[m você pode comprar aproximadamente \033[32mU${dolares:.2f}\033[m')
