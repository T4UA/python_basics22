import csv
lista = []
with open('alunos.csv', 'r') as arquivo:
	file = csv.reader(arquivo)
	header = next(file)
	for linha in file:
		print(linha)
		lista.append(linha)


with open('cp_alunos.csv', 'w', newline='') as copy:
	new_file = csv.writer(copy)
	new_file.writerows(lista)
