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
  print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.")
  print('Existem apenas dois movimentos possíveis:') 
  print('')
  print("  1. Empilhar uma carta sobre a carta imediatamente anterior;") 
  print("  2. Empilhar uma carta sobre a terceira carta anterior.") 
  print('')
  print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:") 
  print('')
  print("  1. As duas cartas possuem o mesmo valor ")
  print('  2. As duas cartas possuem o mesmo naipe.') 
  print('')
  print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.') 
  print('')
  print('Cartas em', colorama.Fore.YELLOW, 'amarelo', colorama.Fore.RESET, 'têm movimentos possíveis')
  print('Cartas em', colorama.Fore.CYAN, 'azul', colorama.Fore.RESET, 'são as últimas empilhadas')
  print('')
  
  print('Aperte [Enter] para iniciar o jogo...')

  input()

def menu():
  utils.limpa_tela()
  imprime_logo()
  print(f"{colorama.Back.CYAN}{colorama.Fore.BLACK}Escolha um modo de jogo")
  print(colorama.Back.RESET, colorama.Fore.RESET)
  print(colorama.Fore.RED,  ' 1 - Texto (todas as cartas abertas)', colorama.Fore.RESET)
  print('  No modo 1, todas as cartas serão visualizadas desde o início')
  print('')
  print(colorama.Fore.MAGENTA,  ' 2 - ASCII ', colorama.Fore.RESET)
  print('  No modo 2, sua mesa se iniciará com 4 cartas e você poderá comprar as demais do monte')
  modo = input()
  return modo