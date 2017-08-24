tempo_máximo_de_vida_de_um_ser_humano= 70

nome = input('Qual o seu nome: ')
print('Seu nome é' + nome)

idade = int(input('Qual a sua idade: '))
print('Você tem ' + str(idade) + ' anos!')

restante = tempo_máximo_de_vida_de_um_ser_humano - idade
print('Você tem ' + str(restante) + ' anos de vida restante')
