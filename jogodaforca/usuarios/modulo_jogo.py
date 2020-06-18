def menu():
    print(' -='*40)
    print('                                           BEM VINDO AO JOGO DA FORCA')
    print(' -='*40)
    print('         !!! A pessoa que irá desafiar, terá que informar uma palavra secreta para o desafiado !!!')
    print('         !!! A pessoa desfiada terá que adivinhar qual palavra secreta é, informando uma letra de cada vez !!!')
    print(' -='*40)
    print()
    return menu

def informar_letra(jogador_desafiado):
    letras = []
    print(f'!!! {jogador_desafiado[0]}, agora é a sua vez de jogar !!!')
    while True:
        letra = input('Informe uma letra --> ')
        if letra not in letras:
            letras.append(letra)
        else:
            print('!!! Você ja informou esta letra !!!')


    return letras

def comparar_letras(letras, palavra):
    letras = []
    for i in range(len(palavra)):
        letras.append(palavra[i])