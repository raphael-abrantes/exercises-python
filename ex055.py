pesoMaior = 0
pesoMenor = 0
for i in range(1,6):
    peso = float(input(f'Digite o {i}° peso: '))
    if i == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print(f'O maior peso é de {pesoMaior:.2f}kg.')
print(f'O menor peso é de {pesoMenor:.2f}kg.')
