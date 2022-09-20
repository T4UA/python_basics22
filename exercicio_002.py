while True:
	idade = int(input('Qual a sua idade? '))
	if 0 < idade < 150:
		print('Proxima pergunta')
		break
	else:
		print('ERRO! Informação invalida')

while True:
	salario = float(input('Informe o seu salario: R$'))
	if salario > 0:
		print('Proxima pergunta')
		break
	else:
		print('ERRO! Informação invalida')

while True:
	sexo = input('Informe seu sexo M ou F: ').strip().upper()[0]
	if 'M' != sexo != 'F':
		print('ERRO! Informação invalida')
	else:
		print('Projeto finalizado')
		break
