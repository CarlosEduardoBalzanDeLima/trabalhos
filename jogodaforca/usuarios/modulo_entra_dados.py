def nome_desafiante(): #informa o nome do desafiante e guarda em uma lista
    desafiante = []
    nome = input('!!! Informe o nome da pessoa que vai ser o desafiante: ')
    desafiante.append(nome)
    return desafiante

def nome_desafiado(): # informa o nome do desafiado e guarda em uma lista
    desafiado = []
    nome = input('!!! Informe o nome da pessoa que vai ser desafiada: ')
    desafiado.append(nome)
    return desafiado

def input_palavra(jogador_desafiante): # pede para o jogador desafiante uma palavra chave
    palavra = input(f'!!! {jogador_desafiante[0]} informe uma palavra para seu amigo(a) adivinhar: ')
    return palavra

def input_dica(jogador_desafiante): # pede para o jogador desafiante informar uma dica
    dica = input('!!! Informe uma dica para seu amigo(a): ')
    return dica

def informar_letra(jogador_desafiado): # agora pede para o jogador desafiado informar uma letra, sendo armazenado todas em uma lista  
    print(f'!!! {jogador_desafiado[0]}, agora é a sua vez de jogar !!!')
    letra = str(input('Informe UMA letra --> '))
    print(' -='*40)
    return letra