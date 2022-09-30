lista = [1, 2, 3,,4, 5, 6, 7, 8, 9]
cont = 0
for elemento in lista:
	if elemento % 2 == 0:
		cont+=1
if cont == 1:
	print(f'Nessa lista tem exatamente {cont} número par')
else:
	print(f'Nessa lista tem exatamente {cont} números pares')
