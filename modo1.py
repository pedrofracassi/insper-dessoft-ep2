import baralho as bar
import colorama

def carta_colorida(carta):
    naipe = bar.extrai_naipe(carta)
    if naipe == '♦' or naipe == '♥':
        return colorama.Fore.RED + carta + colorama.Fore.RESET
    if naipe == '♠' or naipe == '♣':
        return colorama.Fore.WHITE + carta + colorama.Fore.RESET

def renderiza (baralho, ultimo = None):
    for i, carta in enumerate(baralho):
        tem_movs_possiveis = bar.lista_movimentos_possiveis(baralho, i)
        print(colorama.Fore.YELLOW if tem_movs_possiveis else colorama.Fore.WHITE, '{}.'.format(i+1), carta_colorida(carta), (colorama.Fore.CYAN + '<--' + colorama.Fore.RESET) if ultimo == i else '')