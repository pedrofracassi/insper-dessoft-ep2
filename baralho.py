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


def nlembroonome(baralho):
    listanaipe = []
    for carta in baralho:
        if carta[0]+carta[1] == "10":
            if carta[2] not in listanaipe:
                listanaipe.append(carta[2])
        elif carta[1] not in listanaipe:
            listanaipe.append(carta[1])
        else:
            return True 
    listanumero = []
    for carta in baralho:
        if carta[0]+carta[1] == '10':
            if carta[2] not in listanumero:
                listanumero.append(carta[2])
        elif carta[1] not in listanumero:
            listanumero.append(carta[1])
        else:
            return True
    return False      