import random

def gerar_painel():
	cartas = ['iate', 'boné', 'meia']
	random.shuffle(cartas)
	print(cartas)	
	return cartas

def valida_opção(porta, cartas):
	op = input('Temos 3 opções, escolher entre 0, 1 ou 2.')

	if op == 0:
		if cartas[0] == 'iate':
			porta = True

	if op == 1:
		if cartas[1] == 'iate':
			porta = True

	if op == 2:
		if cartas[2] == 'iate':
			porta = True
	return porta, cartas

def altera_porta(porta):
	if porta == True:
		print('Parabéns, Você acertou e ganhou um iate!!')
	if porta == False:
		print('Última chance para trocar de porta!')
		op_porta = input('1.Continuar 2. Trocar de porta')
		if op_porta == 1:
			print('Você perdeuu!!')
		if op_porta == 2:
			valida_opção()
	return porta

cart = gerar_painel()
valida_opção(porta, cartas)
altera_porta()

