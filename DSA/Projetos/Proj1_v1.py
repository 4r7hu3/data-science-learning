import random
from os import system, name

def limpaTela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():
    limpaTela()
    print('\nBem-vindo ao JOGO DA FORCA!')
    print('\nAdivinhe a palavra abaixo:')
    letra_err = []
    
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice(palavras)
    
    t = list('_'*len(palavra))
    chance = len(t)
    
    while chance>0:
        print('')
        print(''.join(t))
        print('\nChances restantes:',chance)
        print('Letras erradas:', letra_err,'\n')
        letra = input('Digite uma letra: ').lower()

        if letra in palavra:
            
            for i in range(chance):
                if palavra[i] == letra:
                    t[i] = letra
        else:
            print('Não há letra \'{}\'!'.format(letra))
            letra_err.append(letra)
            chance-=1
            
        if '_' not in t:
            print('\nParabéns, você acertou a palavra ({})!\n'.format(palavra))
            break
    
    if chance==0:
        print('\nA palavra correta era \'{}\'\n'.format(palavra))
        
game()