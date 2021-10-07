def area(larg, comp):
    a = larg * comp
    print('-='*15)
    print(f'A area de um terreno {larg}x{comp} é = {a:.1f}m²')


print('Área de Terreno')
print('-'*20)
area(float(input('Largura (m): ')),
float(input('Comprimento (m): ')))
