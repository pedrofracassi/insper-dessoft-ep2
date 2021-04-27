import baralho
import utils
import render
import random

def iniciar_jogo ():
    x = baralho.cria_baralho()

    while baralho.possui_movimentos_possiveis(x):
        utils.limpa_tela()
        i=1
        for carta in x:
            print('{}.'.format(i), render.carta_colorida(carta))
            i+=1
        numero=int(input('Escolha uma carta e digite um número entre {} e {}: '.format(1,len(x))))
        while numero>len(x):
            numero=int(input('Escolha uma carta e digite um número entre {} e {}: '.format(1,len(x))))
        while baralho.lista_movimentos_possiveis(x,(numero-1))==[]:
            print('A carta {} não pode ser movida. Por favor, digite um número entre 1 e {} :'.format(1,len(x)))
            numero=int(input('Escolha uma carta e digite um número entre {} e {}: '.format(1,len(x))))
        if len(baralho.lista_movimentos_possiveis(x,(numero-1))) > 0:
            mov = baralho.lista_movimentos_possiveis(x,(numero-1))
            if len(mov)==1:
                novasequencia=baralho.empilha(x,(numero-1),mov[0])
            elif len(mov)>1:
                print('Sobre qual carta você deseja baralho.empilhar? ')
                c0=x[numero-1]
                c1=x[numero-3]           
                print('Qual movimento deseja executar 1 ou 2?')
