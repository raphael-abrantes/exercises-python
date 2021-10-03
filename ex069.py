vTotalMaior18 = 0
vTotalHomens = 0
vTotalMulheresMaior20 = 0

while True:
    #InputArea
    vIdade = int(input('Qual a idade da pessoa? '))
    vSexo = ' '
    while vSexo not in 'MF':
        vSexo = str(input('Qual o sexo da pessoa [M/F]: ')).strip().upper()[0]
    print('-'*33)

    ##Questions
    #Maiores de 18 anos, Homens cadastrados, Mulheres com menos de 20 anos
    if vIdade >= 18:
        vTotalMaior18 = vTotalMaior18 + 1
    if vSexo == 'M':
        vTotalHomens = vTotalHomens + 1
    if vSexo == 'F' and vIdade < 20:
        vTotalMulheresMaior20 = vTotalMulheresMaior20 + 1

    #BreakWhile
    vAns = ' '
    while vAns not in 'YySsNn':
        vAns = str(input('Deseja continuar [Y/N]: '))
    if vAns in 'Nn':
        break
    print('-'*33)

print(f'O total de pessoas com maioridade é: {vTotalMaior18}')
print(f'O total de homens cadastrados foi: {vTotalHomens}')
print(f'O total de mulheres, com menos de 20 anos foi: {vTotalMulheresMaior20}')
print('Fim!')
