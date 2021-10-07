from datetime import datetime
pessoa = dict()
anohoje = datetime.now().year

pessoa['nome'] = str(input('Informe o nome: ')).strip().title()
nasc = int(input('Informe o ano de nascimento: '))
pessoa['idade'] = anohoje - nasc
pessoa['ctps'] = int(input('Informe a CTPS (0 se não tiver): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Informe o ano de contratação: '))
    pessoa['salario'] = float(input('Informe o salário: '))
    faltam = 35 - (anohoje - pessoa['contratacao'])
    pessoa['aposentar'] = pessoa['idade'] + faltam

print('-='*15)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
