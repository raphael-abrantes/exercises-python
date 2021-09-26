km = float(input('Quantos km foram rodados no carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
custo = (60 * dias) + (0.15 * km)
print(f'Um carro que foi alugado por {dias} dias e rodou {km}km, teve o custo de aluguel igual a R${custo:.2f}')
