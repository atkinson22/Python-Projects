estado = 'vez jogador 1'

while True:
    if estado == 'vez jogador 1':
        pass
        estado = 'vez jogador 2'
        continue
    elif estado == 'vez jogador 2':
        pass
    elif estado == 'Fim do Jogo!':
        pass
    else:
        print('ops você atingiu um estado que não existe.')
        break
