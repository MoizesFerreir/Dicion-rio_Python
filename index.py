dicio = dict()

dicio['Nome'] = str(input('Nome do aluno: '))
dicio['Média'] = int(input('Qual a média? '))

if dicio['Média'] >= 7:
    dicio['Situação'] = 'APROVADO'
else:
    dicio['Situação'] = 'REPROVADO'

for k, v in dicio.items():
    print(f'{k} é igual a {v}')
