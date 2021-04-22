import utils

import colorama
colorama.init()

def imprime_logo ():
  print("   ___           _                 _           _                     _                  ")
  print("  / _ \__ _  ___(_) ___ _ __   ___(_) __ _    /_\   ___ ___  _ __ __| | ___  __ _  ___  ")
  print(" / /_)/ _` |/ __| |/ _ \ '_ \ / __| |/ _` |  //_\\\\ / __/ _ \| '__/ _` |/ _ \/ _` |/ _ \ ")
  print("/ ___/ (_| | (__| |  __/ | | | (__| | (_| | /  _  \ (_| (_) | | | (_| |  __/ (_| | (_) |")
  print("\/    \__,_|\___|_|\___|_| |_|\___|_|\__,_| \_/ \_/\___\___/|_|  \__,_|\___|\__,_|\___/ ")
  print("                                                                                        ")

def regras():
  utils.limpa_tela()
  imprime_logo()
  print('pipipi popopo')
  input()

def menu():
  utils.limpa_tela()
  imprime_logo()
  print('Escolha um modo de jogo')
  print('')
  print(colorama.Fore.RED,  ' 1 - Texto (todas as cartas abertas)', colorama.Fore.RESET)
  print('  2 - ASCII')
  modo = input()