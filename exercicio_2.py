idade = int(input('Qual a sua idade? '))
if idade > 150 or idade < 0:
	print('ERRO! Informação invalida')

salario = float(input('Informe o seu salario: '))
if salario < 0:
	print('ERRO! Informação invalida')

sexo = input('Informe seu sexo M ou F: ').upper()
if 'M' != sexo != 'F':
	print('ERRO! Informação invalida')
