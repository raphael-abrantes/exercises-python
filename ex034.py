n = float(input('Digite seu salário: R$'))
if n > 1250:
    nN = n*1.1
    p = 10
else:
    nN = n*1.15
    p = 15
print (f'O salário anterior era de R${n:.2f} e foi ajustado em {p}% para {nN:.2f}')
