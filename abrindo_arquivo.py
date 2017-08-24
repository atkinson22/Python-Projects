fp = open('memoriaspostumas.txt')
l = list(fp)
#print(l)
cont_linha_vazia = 0
total_linhas = 0
for linha in l:
	total_linhas += 1
	if linha == ' \n' or linha == '\n':
		cont_linha_vazia +=1

fp.close()
print(total_linhas)
print(cont_linha_vazia)