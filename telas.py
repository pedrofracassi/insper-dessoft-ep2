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
  print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.")
  print('Existem apenas dois movimentos possíveis:') 

  print("1. Empilhar uma carta sobre a carta imediatamente anterior;") 
  print("2. Empilhar uma carta sobre a terceira carta anterior.") 

  print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:") 

  print("1. As duas cartas possuem o mesmo valor ")
  print('2. As duas cartas possuem o mesmo naipe.') 

  print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.') 

  print('Aperte [Enter] para iniciar o jogo...')

  input()

def menu():
  utils.limpa_tela()
  imprime_logo()
  print('Escolha um modo de jogo')
  print('')
  print(colorama.Fore.RED,  ' 1 - Texto (todas as cartas abertas)', colorama.Fore.RESET)
  print('  2 - ASCII')
  modo = input()