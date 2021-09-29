s = 0
for n in range(1,501,2):
    if n % 3 == 0:
        #s += n
        s = s + n
print(f'A soma dos valores impares e múltiplos de três é {s}')
