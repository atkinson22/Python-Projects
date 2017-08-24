nome = input('Qual o seu nome? ')

if nome == 'Apolo':
	print('Saiaaa')
	exit()
dinheiro = int(input('Digite quanto dinheiro você tem no banco: '))

if dinheiro < 0:
	while(true):
		print('Apenas números positivos!')

if dinheiro < 100:
	print('oprimido pela sociedade capitalista!')

if dinheiro > 100:
	print('Burguês filha da puta!')

if dinheiro == 100:
	print('Apenas classe média!')

print('fim do programa')
