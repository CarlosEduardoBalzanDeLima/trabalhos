from usuarios.modulo_entra_dados import nome_desafiante, nome_desafiado, input_palavra, input_dica, informar_letra
from usuarios.modulo_jogo import menu
from interface.modulo_forca import mostrar_forca

menu()

jogador_desafiante = nome_desafiante()
jogador_desafiado = nome_desafiado()
print()
palavra = input_palavra(jogador_desafiante)
dica = input_dica(jogador_desafiante)
print()
print(' -='*40)
letras = informar_letra(jogador_desafiado)
mostrar_forca(0, len(palavra), dica, letras)
informar_letra(jogador_desafiado)
