def meu_abs(n):
	ret = ''
	str_n = str(n)
	if str_n[0] == '-':
		ret = str_n[1:len(str_n)]
	else:
		ret = str_n

def raiz_quadrada(n):
	res = n**(1/2)
	return res

def meu_len(l):
	i = 0
	cont = 0
	for i in l:
		cont = cont + i
	return cont

def meu_max(l):
	re = l[0]

	for numero in l:
		if número > ret:
			ret = numero
	return ret

def meu_min(l):
	l = list(1, 2, 3, 4)
	res = min(l)
	return res

def meu_sum(l):
	ret = 0
	for numero in l:
		ret =+ numero

	return ret

def media(l):
	soma = meu_sum(l)
	tamanho = meu_len(l)
	ret = soma/tamanho


print(meu_abs(-1) == 1)
print(meu_abs(1) == 1)
print(meu_abs(0) == 0)
print(meu_abs(10) == 10)
print(meu_abs(-10) == 10)

print('raiz_quadrada(4) == 2.0')
print(raiz_quadrada(4) == 2.0)

print('raiz_quadrada(9) == 3.0')
print(raiz_quadrada(9) == 3.0)

print(meu_len([]) == 0)
print(meu_len([6]) == 1)
print(meu_len([6, 11]) == 2)

print('meu_sum([9, 9]) == 18')
print(meu_sum([9, 9]) == 18)
print('meu_sum([9, 9]) == 18')
print(meu_sum([1, 1]) == 2)
