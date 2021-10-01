somaIdade = 0
mediaIdade = 0
maiorIdadeM = 0
nomeMVelho = ''
countF = 0
for i in range(1,5):
    print(f'----- {i}° Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade = somaIdade + idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeM = idade
        nomeMVelho = nome
    if sexo in 'Mm' and idade < maiorIdadeM:
        maiorIdadeM = idade
        nomeMVelho = nome
    if sexo in 'Ff' and idade < 20:
        countF = countF + 1
mediaIdade = somaIdade / 4
print(f'A média de idade das pessoas é de {mediaIdade}')
print(f'O homem mais velho é o {nomeMVelho} com {maiorIdadeM} anos')
print(f'Existem {countF} mulheres com menos de 20 anos')
