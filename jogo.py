import time
# máquina finita de estados
lugar = 'Inferno'

#lugar 

while(True):
    print('carregando lugar...')
    time.sleep(.2)
    print('.')
    time.sleep(.2)
    print('.')
    time.sleep(.1)
    print('.')
    if lugar == 'Casa do Jogador':
        print('Você nasceu e está na sua casa!')
        print('Para onde deseja ir?')
        opção1 = 'Rua'
        opção2 = 'Cano de casa'
        print('Sua opções: 1.'+ opção1 + '2. ' + opção2)
        opçãoescolhida = input('Digite sua opção: ')
        if opçãoescolhida == '1':
            lugar = opção1
        if opçãoescolhida == '2':
            lugar = opção2
    elif lugar == 'Iate':
            print('Você venceu!')
            break    
    elif lugar == 'Inferno':      
        lugar = input('Você está na casa do diabo, para onde deseja ir?')
        opção1 = 'Quintos do Inferno'
        opção2 = 'Voltar para a terra!'
        opção3 = 'Céu'
        print('Sua opções: 1.'+ opção1 + '2. ' + opção2 + '3. ' + opção3)
        opçãoescolhida = input('Digite sua opção: ')
        if (opçãoescolhida == 1):
            print('Então abraça o capeta!!')
        elif (opçãoescolhida == 2):
            print('Para voltar para a terra você precisa fazer esse cálculo.')
            print('Resolva: 2 * 2')
            resposta = int(input())
            if resposta == 2*2:
                print('Parabéns você voltará para a sua casa')
                continue
            else:
                print('Vai ficar aí mesmo!!')
        elif opçãoescolhida == 3:
            print('Para voltar para a terra você precisa fazer esse cálculo.')
            print('Resolva: 5 * 5')
            resposta = int(input())
            if resposta == 5*5:
                print('Parabéns você voltará para a sua casa')
                continue
            else:
                print('Vai ficar aí mesmo!!')      
    elif lugar == 'Rua':
        print('Daqui você pode ir pra frente na vida!')
        opção1 = 'Roubar um banco'
        opção2 = 'Fazer conta'
        opção3 = 'Fazer nada'
        print('Sua opções: 1.'+ opção1 + '2. ' + opção2)
        opçãoescolhida = input('Digite sua opção: ')
        if opçãoescolhida == '1':
            lugar = 'Cadeia'
        elif opçãoescolhida == '2':
            print('Resolva essa conta aqui: 1 + 1')
            resposta = int(input('Resposta da conta: '))
            if resposta == 1 + 1:
                lugar = 'Iate'
            else:
                lugar = 'Casa do Jogador'
        elif opçãoescolhida == '3':
            print('Você não fez nada')
    elif lugar == 'Cano de casa':
        print('Daqui você se dará mal.')
        lugar = 'Inferno'
    elif lugar == 'Cadeia':
        print('Você tentou roubar um banco e foi preso')
        print('Você vai ficar aqui para sempre')
        input()
    elif lugar == 'Frente do Iate':
        print('Pra entrar no iate é necessário uma chave')
        if temchave:
            
print('GAME OVER')
