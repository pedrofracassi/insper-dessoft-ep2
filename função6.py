def extrai_naipe(carta):
    if len(carta)==3:
        return carta[2]
    else:    
        return carta[1]
def extrai_valor(carta):
    if len(carta)==3:
        return carta[0]+carta[1]
    else:
        return carta[0]    
def possui_movimentos_possiveis(baralho):
    i=0
    o=1
    while len(baralho) >o:
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

print(possui_movimentos_possiveis(['A♦', 'J♥', 'Q♣', 'K♠', '10♣']))                     
                  