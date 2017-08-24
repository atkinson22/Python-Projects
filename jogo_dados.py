import random

#input
#random.randrange
#if
#==

#joga um dado de 6 lados

# o usuário tem que advinhar qual é o numero
opcsair = 0
nome = input('Qual o seu nome? ')
tentativas = 0

while (tentativas <= 3):
    opc = int(input('Qual o seu papite de 1 a 6? '))
    dado = random.randrange(1,7)
    tentativas = tentativas + 1
    
    if opc == dado:
        print('Número sorteado: '+str(dado))
        print('Seu palpite: '+ str(opc))

    if opc != dado:
        print('Número sorteado: '+str(dado))
        print('Você errou!!')

saida =input('Deseja continuar jogando(s/n)? ')
if saida == 's':
    opcsair = 0
if saida == 'n':
    exit()
