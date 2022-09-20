sumList = []
def soma(l1, l2):
	count = 0
	for i in range(len(l1)):
		soma = l1[count] + l2[count]
		sumList.append(soma)
		count+=1
	return sumList

listaUm = [1,4,3]
listaDois = [3,5,1]

print(soma(listaUm, listaDois))
