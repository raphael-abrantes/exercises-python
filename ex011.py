alt = float(input('Qual é a altura da parede? '))
larg = float(input('Qual é a largura da parede? '))
area = alt * larg
litros = area / 2
print (f'Serão necessários {litros:.21}L de tinta para pintar uma parede de {area:.1f}m²')
