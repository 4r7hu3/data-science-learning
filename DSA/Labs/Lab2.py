print('\n********** Calculadora em Python **********\n')

print('Selecione o número da operação desejada: \n')

print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n')

opt = int(input('Digite sua opção (1/2/3/4): '))

n1 = float(input('\nDigite o primeiro número: '))
n2 = float(input('\nDigite o segundo número: '))

print('\n')

def soma(a,b):
    return a+b

def sbtr(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

if opt == 1:
    print(n1, '+', n2, '=', round(soma(n1,n2), 3), '\n')
elif opt == 2:
    print(n1, '-', n2, '=', round(sbtr(n1,n2), 3), '\n')
elif opt == 3:
    print(n1, 'x', n2, '=', round(mult(n1,n2), 3), '\n')
elif opt == 4:
    print(n1, '/', n2, '=', round(div(n1,n2), 3), '\n')
else:
    print('Digite uma opção válida!\n')