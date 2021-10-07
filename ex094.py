pessoa = dict()
cadastro = list()
media = totidade = 0

while True:
    print('=-'*20)
    pessoa['nome'] = str(input('Digite o nome: ')).strip().title()
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('Digite o sexo [M/F]: ').strip().upper()[0]
    pessoa['idade'] = int(input('Digite a idade: '))
    cadastro.append(pessoa.copy())

    resposta = ' '
    while resposta not in 'SN':
        print('=-'*20)
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break

print('=-'*20)
print(f'- O grupo tem {len(cadastro)} pessoas.')
for p in cadastro:
    totidade += p['idade']
media = totidade / len(cadastro)
print(f'- A média de idade é de {media:.2f} anos')
print('- As mulheres cadastradas foram: ',end=' ')
for p in cadastro:
    if p['sexo'] == 'F':
        print(p['nome'], end=', ')
print()
print('- Lista das pessoas que estão acima da média de idade:')
for p in cadastro:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}',end='; ')
        print()
print('=-'*20)
print('FIM DO PROGRAMA')
