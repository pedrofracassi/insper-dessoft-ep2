from baralho import cria_baralho
from baralho import possui_movimentos_possiveis
from baralho import lista_movimentos_possiveis
from baralho import empilha
x= cria_baralho()
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
    return 'Que pena,você perdeu!Continue tentando'
if len(x)==1:
    return 'Parabéns,você ganhou!'                      



   









    