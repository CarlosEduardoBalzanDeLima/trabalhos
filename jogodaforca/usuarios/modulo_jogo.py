def dividir_palavra(palavra): #adiciona todas as letras da palavra em uma lista
    lista_letras = []
    for i in range(len(palavra)):
        lista_letras.append(palavra[i])
    return lista_letras

def esconder(palavra): #esconde a palavra
    palavra_escondida = []
    for n in range(0, len(palavra)):
        palavra_escondida.append('_')
    return palavra_escondida