# função que recebe uma lista de números e retorne uma nova lista com o dobro desses números

def dobro_lista(l):
	ret = []
	for numero in l:
		ret.append(numero*2)
	return ret

print(dobro_lista([2, 3])==([4, 6]))