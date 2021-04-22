from baralho import cria_baralho
from baralho import possui_movimentos_possiveis
from baralho import lista_movimentos_possiveis
from baralho import empilha
import random
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
            pergunta1 = int(input('Qual movimento deseja executar {} ou {}?'.format(mov[0],mov[1])))
            novasequencia=(x,numero-1,mov[pergunta1])  
    x=novasequencia       
#TODO: MEXER NA LINHA 22 PRA APARECER A CARTA AO INVES DO MOVIMENTO 
# TODO:POR COR
# TODO: MENSAGEM SE PERDER OU GANHAR    
                  



   









    