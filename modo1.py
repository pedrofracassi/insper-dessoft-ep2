import baralho
import colorama

def carta_colorida(carta):
    naipe = baralho.extrai_naipe(carta)
    if naipe == '♦' or naipe == '♥':
        return colorama.Fore.RED + carta + colorama.Fore.RESET
    if naipe == '♠' or naipe == '♣':
        return colorama.Fore.WHITE + carta + colorama.Fore.RESET

def renderiza (baralho):
    for i, carta in enumerate(baralho):
        print('{}.'.format(i), carta_colorida(carta))