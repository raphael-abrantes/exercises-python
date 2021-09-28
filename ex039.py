from datetime import date
hoje = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = hoje - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {hoje}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para se alistar')
    print(f'Seu alistamento será em {nasc + 18}')
else:
    print(f'Já se alistou a {idade - 18} anos')
