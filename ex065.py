answer = 'S'
i = s = maior = menor = 0
while answer in 'YySs':
    i = i + 1
    n = int(input('Digite um valor: '))
    answer = str(input('Deseja cotinuar [Y/N]? ')).upper().strip()[0]
    if answer not in 'YySsNn':
        while answer not in 'YySsNn':
            answer = str(input('Opção inválida. Deseja cotinuar [Y/N]? ')).upper().strip()[0]
    if i == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    s = s + n
print(f'A média dos {i} valores digitados é {s/i:.2f}')
print(f'O menor valor digitado foi {menor} e o maior foi {maior}')
