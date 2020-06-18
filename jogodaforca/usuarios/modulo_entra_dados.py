def nome_desafiante():
    desafiante = []
    nome = input('!!! Informe o nome da pessoa que vai ser o desafiante: ')
    desafiante.append(nome)
    pontos = 0
    desafiante.append(pontos)
    return desafiante

def nome_desafiado():
    desafiado = []
    nome = input('!!! Informe o nome da pessoa que vai ser desafiada: ')
    desafiado.append(nome)
    pontos = 0
    desafiado.append(pontos)
    return desafiado

def input_palavra(jogador_desafiante):
    palavra = input(f'!!! {jogador_desafiante[0]} informe uma palavra para seu amigo(a) adivinhar: ')
    return palavra

def input_dica(jogador_desafiante):
    dica = input('!!! Informe uma dica para seu amigo(a): ')
    return dica

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
