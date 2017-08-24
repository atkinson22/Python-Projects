def tres():
	ret = 3
	return ret

def dobro(n):
	n = n * 2
	return n

def multiplica_dois_números(x, y):
	ret = x * y
	return ret

def somar_dois_números(x, y):
	ret = x + y
	return ret

def somar_tres_numeros(x, y, z):
	ret = x + y + z
	return ret

def produto(l):
	ret = 1
	for elemento in l:
		ret *= elemento
	return ret

def meu_sum(l):
	ret = 0 
	for elemento in l:
		ret += elemento
	return ret

# função que pega uma lista

print(tres())
print(dobro(3))
l = [1, 4, 4]
print(somar_dois_números(5, 7))
print(produto([1, 4, 4]))