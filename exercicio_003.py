cont = 0

perg_1 = input('Mora perto da vitima? S OU N: ').strip().upper()[0]
if perg_1 == 'S':
	cont += 1
perg_2 = input('Já trabalhou com a vitima? S ou N: ').strip().upper()[0]
if perg_2 == 'S':
	cont += 1
perg_3 = input('Telefonou para a vitima? S ou N: ').strip().upper()[0]
if perg_3 == 'S':
	cont += 1
perg_4 = input('Esteve no local do crime? S ou N: ').strip().upper()[0]
if perg_4 == 'S':
	cont += 1
perg_5 = input('Devia para a vitima? S ou N: ').strip().upper()[0]
if perg_5 == 'S':
	cont += 1


if cont == 5:
	print('Voce é o assassino(a)!')
elif cont == 4 or count == 3:
	print('Voce é cumplice')
elif cont == 2:
	print('Voce é apenas suspeito(a)')
elif cont <= 1:
	print('Voce esta liberado(a)')
else:
	print('ERRO')
