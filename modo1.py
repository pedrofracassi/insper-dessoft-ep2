import baralho
import utils
import render
import random

def renderiza (baralho):
    for i, carta in enumerate(baralho):
        print('{}.'.format(i), render.carta_colorida(carta))