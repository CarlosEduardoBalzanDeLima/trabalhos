from usuarios.modulo_entra_dados import nome_desafiante, nome_desafiado, input_palavra, input_dica, informar_letra
from usuarios.modulo_jogo import dividir_palavra, esconder
from interface.modulo_forca import mostrar_forca
from interface.modulo_sai_dados import menu, jogo
import os

menu()

jogador_desafiante = nome_desafiante() # nome desafiante
jogador_desafiado = nome_desafiado() # nome desafiado
print()

palavra = input_palavra(jogador_desafiante) # palavra chave
dica = input_dica(jogador_desafiante) # palavra dica

os.system('cls') or None # limpa terminal

palavra_em_lista = dividir_palavra(palavra) # coloca a palavra secreta em uma lista
esconde_palavra = esconder(palavra) # substitui palavra pelo traço '_'

jogo()

erros = 0
letras_informadas = []
while True:
    mostrar_forca(erros, dica, letras_informadas, esconde_palavra) # imprime a forca
    while True:
        print(' -='*40)
        letra = informar_letra(jogador_desafiado) # pede para o desafiado informar as letras
        if len(letra) != 1:
            print('Informe apenas uma letra!')
        else:
            if letra in letras_informadas:
                print(f'A letra {letra} ja foi informada!')
            else:
                break
    letras_informadas.append(letra)

    if letra in palavra:
        posicoes = []
        for i, n in enumerate(palavra):
            if letra == n:
                esconde_palavra[i] = n
                posicoes.append(i)

        if palavra_em_lista == esconde_palavra:
            mostrar_forca(erros, dica, letras_informadas, esconde_palavra) # imprime a forca
            print('!!! PARABENS VOCÊ GANHOU !!!')
            break

    else:
        erros += 1
        if erros == 6:
            mostrar_forca(erros, dica, letras_informadas, esconde_palavra) # imprime a forca
            print('!!! INFELIZMENTE VOCÊ PERDEU !!!')
            print(f'A palavra era {palavra}!')
            break
