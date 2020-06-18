def menu():
    print(' -='*40)
    print('                                           BEM VINDO AO JOGO DA FORCA')
    print(' -='*40)
    print('         !!! A pessoa que irá desafiar, terá que informar uma palavra secreta para o desafiado !!!')
    print('         !!! A pessoa desfiada terá que adivinhar qual palavra secreta é, informando uma letra de cada vez !!!')
    print(' -='*40)
    print()
    return menu


def comparar_letras(letras, palavra):
    letras = []
    for i in range(len(palavra)):
        letras.append(palavra[i])