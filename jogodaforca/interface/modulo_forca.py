def mostrar_forca(erros, palavra, dica, letras):
    if erros == 0:
        print()
        print("_______ ")                
        print("|                                   " "===== DICA: {} =====".format(dica))
        print("|   ")           
        print("|                                   " "===== LETRAS JA INFORMADAS: !! {} !! =====".format(letras))                      
        print("|   ")
        print("|   ")
        print("_"*palavra)
        print()
    elif erros == 1:
        print()
        print("_______ ")
        print("|    |                              " "===== DICA: {} =====".format(dica))
        print("|   ")
        print("|                                   " "===== LETRAS JA INFORMADAS: !! {} !! =====".format(letras))   
        print("|   ")
        print("|   ")
        print("_"*palavra)
        print()
    elif erros == 2:
        print()
        print("_______ ")
        print("|    |                              " "===== DICA: {} =====".format(dica))
        print("|    O ")
        print("|                                   " "===== LETRAS JA INFORMADAS: !! {} !! =====".format(letras))   
        print("|   ")
        print("|   ")
        print("_"*palavra)
        print()
    elif erros == 3:
        print()
        print("_______ ")
        print("|    |                              " "===== DICA: {} =====".format(dica))
        print("|    O ")
        print("|    |                              " "===== LETRAS JA INFORMADAS: !! {} !! =====".format(letras))   
        print("|   ")
        print("|   ")
        print("_"*palavra)
        print()
    elif erros == 4:
        print()
        print("_______ ")
        print("|    |                              " "===== DICA: {} =====".format(dica))
        print("|    O ")
        print("|   /|\\                            " "===== LETRAS JA INFORMADAS: !! {} !! =====".format(letras))   
        print("|   ")
        print("|   ")
        print("_"*palavra)
        print()
    elif erros == 5:
        print()
        print("_______ ")
        print("|    |                              " "===== DICA: {} =====".format(dica))
        print("|    O ")
        print("|   /|\\                            " "===== LETRAS JA INFORMADAS: !! {} !! =====".format(letras))   
        print("|    |")
        print("|   ")
        print("_"*palavra)
        print()
    elif erros == 6:
        print()
        print("_______ ")
        print("|    |                              " "===== DICA: {} =====".format(dica))
        print("|    O ")
        print("|   /|\\                            " "===== LETRAS JA INFORMADAS: !! {} !! =====".format(letras))   
        print("|    | ")
        print("|   / \\ ")
        print("_"*palavra)
        print()