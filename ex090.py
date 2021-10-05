aluno = {'nome':'' , 'media':0.0 , 'situacao':''}

aluno['nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

aluno['situacao'] = 'Aprovado' if aluno['media'] >= 7.0 else 'Reprovado'

print('-='*15)
print(f'O nome é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
print(f'A situação é {aluno["situacao"]}')
