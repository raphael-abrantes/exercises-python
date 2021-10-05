from time import sleep
listAlunos = list()
listAluno = list()
listNotas = list()

while True:
    totnota = 0.0
    print('-'*40)
    listAluno.append(str(input('Nome: ')).strip().title())
    for n in range(0, 2):
        nota = float(input(f'Nota {n+1}: '))
        totnota += nota
        listNotas.append(nota)
    media = totnota / 2
    listAluno.append(listNotas[:])
    listAluno.append(media)
    listAlunos.append(listAluno[:])
    listNotas.clear()
    listAluno.clear()

    print('-'*40)
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-=-'*20)
print(f'{"Nº":<5}{"NOME":<25}{"MÉDIA":>}')
print('-'*35)
for i, a in enumerate(listAlunos):
   print(f'{i:<5}{a[0]:<25}{a[2]:>5.1f}')

while True:
    print('-'*35)
    opcao = int(input('Mostrar notas de qual aluno?[999 para sair]: '))
    if opcao == 999:
        break
    alunoop = listAlunos[opcao]
    print(f'As notas de {alunoop[0]} são: {alunoop[1]}')
print('-=-'*5)
print('FINALIZANDO...')
sleep(2)
print('-=-'*5)
print('Fim do Programa!')
print("-=-"*5)
