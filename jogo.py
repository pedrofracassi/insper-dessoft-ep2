import baralho
import utils
import render

def iniciar (renderiza_cartas):
    x = baralho.cria_baralho()

    while baralho.possui_movimentos_possiveis(x):
        utils.limpa_tela()
        renderiza_cartas(x)
        numero=int(input('Escolha uma carta e digite um número entre {} e {}: '.format(1,len(x))))
        if numero>len(x):
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
                print('1. {}'.format(c0)) 
                print('2. {}'.format(c1))
                pergunta1 = int(input(' '))
                novasequencia=baralho.empilha(x,numero-1,mov[pergunta1-1])  
        x=novasequencia

    if len(x)>1:
        utils.limpa_tela()
        renderiza_cartas(x)
        print('Que pena, você perdeu! Continue tentando.')

    if len(x)==1:
        utils.limpa_tela()
        renderiza_cartas(x)
        print('Parabéns, você ganhou!')