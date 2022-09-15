lista = [1, 2, 3,,4, 5, 6, 7, 8, 9]
count = 0
for i in lista:
	if i % 2 == 0:
		count+=1
if count == 1:
	print(f'Nessa lista tem exatamente {count} número par')
else:
	print(f'Nessa lista tem exatamente {count} números pares')
