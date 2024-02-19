import random
from os import system, name

def limpaTela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def mostra_boneco(chances):
    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def game():
    limpaTela()
    print('\nBem-vindo ao JOGO DA FORCA!')
    print('\nAdivinhe a palavra abaixo:')
    letra_err = []
    
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice(palavras)
    
    t = list('_'*len(palavra))
    chances = 6
    
    while chances>0:
        print(''.join(t))
        print('')
        print(mostra_boneco(chances))
        print('\nChances restantes:',chances)
        print('Letras erradas:', letra_err,'\n')
        letra = input('Digite uma letra: ').lower()

        if letra in palavra:
            
            for i in range(len(t)):
                if palavra[i] == letra:
                    t[i] = letra
        else:
            print('Não há letra \'{}\'!'.format(letra))
            letra_err.append(letra)
            chances-=1
            
        if '_' not in t:
            print('\nParabéns, você acertou a palavra ({})!\n'.format(palavra))
            break
    
    if chances==0:
        print(mostra_boneco(chances))
        print('\nA palavra correta era \'{}\'...\n'.format(palavra))
        
game()