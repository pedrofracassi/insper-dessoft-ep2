import baralho as bar
import colorama

def carta_colorida(carta):
    naipe = bar.extrai_naipe(carta)
    if naipe == '♦' or naipe == '♥':
        return colorama.Fore.RED + carta + colorama.Fore.RESET
    if naipe == '♠' or naipe == '♣':
        return colorama.Fore.WHITE + carta + colorama.Fore.RESET

def renderiza (baralho):
    for i, carta in enumerate(baralho):
        tem_movs_possiveis = bar.lista_movimentos_possiveis(baralho, i)
        print(colorama.Fore.YELLOW if tem_movs_possiveis else colorama.Fore.WHITE, '{}.'.format(i), carta_colorida(carta))