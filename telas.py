import utils

import colorama
colorama.init()

def imprime_logo ():
  print(colorama.Fore.RED, "   ___           _                 _       ", colorama.Fore.CYAN, "    _                     _                  ")
  print(colorama.Fore.RED, "  / _ \__ _  ___(_) ___ _ __   ___(_) __ _ ", colorama.Fore.CYAN, "   /_\   ___ ___  _ __ __| | ___  __ _  ___  ")
  print(colorama.Fore.RED, " / /_)/ _` |/ __| |/ _ \ '_ \ / __| |/ _` |", colorama.Fore.CYAN, "  //_\\\\ / __/ _ \| '__/ _` |/ _ \/ _` |/ _ \ ")
  print(colorama.Fore.RED, "/ ___/ (_| | (__| |  __/ | | | (__| | (_| |", colorama.Fore.CYAN, " /  _  \ (_| (_) | | | (_| |  __/ (_| | (_) |")
  print(colorama.Fore.RED, "\/    \__,_|\___|_|\___|_| |_|\___|_|\__,_|", colorama.Fore.CYAN, " \_/ \_/\___\___/|_|  \__,_|\___|\__,_|\___/ ")
  print(colorama.Fore.RESET)

def regras():
  utils.limpa_tela()
  imprime_logo()
  print('pipipi popopo')
  input()

def menu():
  utils.limpa_tela()
  imprime_logo()
  print(f"{colorama.Back.CYAN}{colorama.Fore.BLACK}Escolha um modo de jogo")
  print(colorama.Back.RESET, colorama.Fore.RESET)
  print(colorama.Fore.RED,  ' 1 - Texto (todas as cartas abertas)', colorama.Fore.RESET)
  print('  2 - ASCII')
  modo = input()
  return modo