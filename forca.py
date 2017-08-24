import getpass

palavra_secreta = getpass.getpass('Digite a palavra a ser advinhada: ')

tamanho_palavra_secreta = len(palavra_secreta)
chances_de_acertar = tamanho_palavra_secreta

letras_que_o_jogador_digitou = ''

while True:

    painel = ''
    for letra in palavra_secreta:
        if letra in letras_que_o_jogador_digitou:
            painel += '[' + letra + ']'
        else:
            painel += '[*]'

    print(painel)
    todas_as_letras_dentro_da_palavra_secreta = False
    for letra in palavra_secreta:
        if letra in letras_que_o_jogador_digitou:
            todas_as_letras_dentro_da_palavra_secreta = True
        else:
            todas_as_letras_dentro_da_palavra_secreta = False
            break

    if todas_as_letras_dentro_da_palavra_secreta:
        print('Você venceu o jogo!')
        break

    palpite = input(' Digite uma letra: ')

    # NOTE(atkinson22): guards para evitar que o usuário trapaceie digitando mais que uma letra
    if palpite == '':
        continue

    if len(palpite) > 1:
        continue

    letras_que_o_jogador_digitou = letras_que_o_jogador_digitou + palpite
    letras_que_o_jogador_digitou += palpite
    print('                      ---------------------------------')
    print('                      Letras que o jogador digitou: ' + letras_que_o_jogador_digitou.upper())
    print('                      ---------------------------------')
    print('                      Chances de acertar: ' + str(chances_de_acertar)) 
    print('                      ---------------------------------')
    print('                      Tamanho palavra secreta: ' + str(tamanho_palavra_secreta))
    print('                      ---------------------------------')

    if palpite == '':
        continue
    
    if len(palpite) > 1:
        continue
    
    if palpite in palavra_secreta:
        print('Você acertou!')
        print(palpite.upper() + ' está dentro da palavra!')
    else:
        print(palpite.upper() + ' não está dentro da palavra...')
        chances_de_acertar -= 1
    
    if chances_de_acertar == 0:
        print('Acabou suas tentativas!')
        break
print('Fim do jogo')
