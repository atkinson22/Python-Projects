#! /usr/bin/env python3

def imprimir_caixa(tamanho_da_tampa):
	print('-'*tamanho_da_tampa)
	print('|' + ' '*(tamanho_da_tampa-2)+ '|')
	print('|' + ' '*(tamanho_da_tampa-2)+ '|')
	print('|' + ' '*(tamanho_da_tampa-2)+ '|')
	print('-'*tamanho_da_tampa)
	return None

#essa variável contém o tamanho que vai ser a tampa
tamanho_da_tampa = int(input('Digite o tamanho da tampa: '))
imprimir_caixa(tamanho_da_tampa)
