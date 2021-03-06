import random

def extrai_valor(carta):
    if len(carta)==3:
        return carta[0]+carta[1]
    else:
        return carta[0]

def extrai_naipe(carta):
    if len(carta)==3:
        return carta[2]
    else:    
        return carta[1]

def cria_baralho():
    baralho = ['2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','A♠','K♠','Q♠','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','A♥','K♥','Q♥','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','A♦','K♦','Q♦','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','A♣','K♣','Q♣']
    random.shuffle(baralho)
    return baralho

def lista_movimentos_possiveis (baralho, i):
    movs_validos = [1, 3]
    movs_possiveis = []

    for mov in movs_validos:
        if i < mov:
            continue
        if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-mov]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-mov]):
            movs_possiveis.append(mov)

    return movs_possiveis
    
def empilha(lista, ppartida, pchegada):
    lista[pchegada] = lista[ppartida]
    del lista[ppartida]
    return lista
   
def possui_movimentos_possiveis(mesa, monte):
    baralho = mesa + monte
    i=0
    o=1
    while len(baralho) > o:
        if extrai_naipe(baralho[i])==extrai_naipe(baralho[o]) or extrai_valor(baralho[i])==extrai_valor(baralho[o]):
            return True
        i+=1
        o=i+1
    baralhoinvertido = []
    i=len(baralho) - 1
    while i>0:
        baralhoinvertido.append(baralho[i])
        i-=1
    i=0
    o=3
    while len(baralho)>o+1:
        if extrai_naipe(baralho[i])==extrai_naipe(baralho[o]) or extrai_valor(baralho[i])==extrai_valor(baralho[o]):
            return True
        i+=1
        o=i+3
    return False   