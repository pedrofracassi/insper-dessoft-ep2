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
                  