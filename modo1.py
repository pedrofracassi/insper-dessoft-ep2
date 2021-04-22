from baralho import cria_baralho
from baralho import possui_movimentos_possiveis
from baralho import lista_movimentos_possiveis
from baralho import empilha
from baralho import extrai_naipe
import colorama
x= cria_baralho()
def pinta_baralho(x):
    for carta in x:
        if extrai_naipe(carta) == '♠':
            carta = colorama.Fore.RED, '{}'.format(carta),colorama.Fore.RESET
        if extrai_naipe(carta)== '♦':
            carta = colorama.Fore.CYAN,'{}'.format(carta),colorama.Fore.RESET
        if extrai_naipe(carta) == '♥':
            carta = colorama.Fore.MAGENTA,'{}'.format(carta),colorama.Fore.RESET
        else:
            carta = colorama.Fore.YELLOW,'{}'.format(carta),colorama.Fore.RESET                
    return x
y= cria_baralho()
x = pinta_baralho(y)            
while possui_movimentos_possiveis(x):
    i=1
    for carta in x:
        print('{}.'.format(i),carta)
        i+=1
    numero=int(input('Escolha uma carta e digite um número entre {} e {}: '.format(1,len(x))))
    if lista_movimentos_possiveis(x,(numero-1))==[]:
        print('A carta {} não pode ser movida. Por favor, digite um número entre 1 e {} :'.format(1,len(x)))
        numero=int(input('Escolha uma carta e digite um número entre {} e {}: '.format(1,len(x))))
    if len(lista_movimentos_possiveis(x,(numero-1))) > 0:
        mov = lista_movimentos_possiveis(x,(numero-1))
        if len(mov)==1:
            novasequencia=empilha(x,(numero-1),mov[0])
        elif len(mov)>1:
            print('Sobre qual carta você deseja empilhar? ')
            c0=x[numero-1]
            c1=x[numero-3]           
            print('Qual movimento deseja executar 1 ou 2?')
            print('1. {}'.format(c0)) 
            print('2. {}'.format(c1))
            pergunta1 = int(input(' '))
            novasequencia=empilha(x,numero-1,mov[pergunta1-1])  
    x=novasequencia       
if len(x)>1:
    print('Que pena,você perdeu!Continue tentando')
if len(x)==1:
    print('Parabéns,você ganhou!')                      



   









    