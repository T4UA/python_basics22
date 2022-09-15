count = 0

perg_1 = input('Mora perto da vitima? S OU N: ').upper()[0].strip()
if perg_1 == 'S':
	count += 1
perg_2 = input('Já trabalhou com a vitima? S ou N: ').upper()[0].strip()
if perg_2 == 'S':
	count += 1
perg_3 = input('Telefonou para a vitima? S ou N: ').upper()[0].strip()
if perg_3 == 'S':
	count += 1
perg_4 = input('Esteve no local do crime? S ou N: ').upper()[0].strip()
if perg_4 == 'S':
	count += 1
perg_5 = input('Devia para a vitima? S ou N: ').upper()[0].strip()
if perg_5 == 'S':
	count += 1


if count == 5:
	print('Voce é o assassino(a)!')
elif count == 4 or count == 3:
	print('Voce é cumplice')
elif count == 2:
	print('Voce é apenas suspeito(a)')
elif count <= 1:
	print('Voce esta liberado(a)')
else:
	print('ERRO')
