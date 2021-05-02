import baralho
import colorama
import os
import math

# TODO: Cores das cartas
# TODO: Posicionamento melhor dos naipes

largura_carta = 11

def carta_ascii (carta, numero_carta):
  naipe = baralho.extrai_naipe(carta)
  valor = baralho.extrai_valor(carta)

  espaco = ' '
  if valor == '10':
    espaco = 0
    valor = 1

  valor_id = numero_carta
  espaco_id = ' '
  if valor_id > 9:
    valor_id = str(numero_carta)[0]
    espaco_id = str(numero_carta)[1]

  return [
    '┌─────────┐',
    '│{}{}       │'.format(valor, espaco),
    '│         │',
    '│         │',
    '│    {}    │'.format(naipe),
    '│         │',
    '│         │',
    '│       {}{}│'.format(valor, espaco),
    '└─────────┘',
    '     {}{}    '.format(valor_id, espaco_id)
  ]

def linha_cartas (mesa, cartas, ultimo = None, offset = 0):
  cartas_ascii = []

  for i, carta in enumerate(cartas):
    i_total_carta = offset + i
    numero_carta = i_total_carta + 1
    cartas_ascii.append(carta_ascii(carta, numero_carta))

  linhas = []
  
  for ic, carta in enumerate(cartas_ascii):
    i_total_carta = offset + ic
    for i, linha in enumerate(carta):

      if len(linhas) < len(carta):
        linhas.append("")

      if len(baralho.lista_movimentos_possiveis(mesa, i_total_carta)):
        color = colorama.Fore.YELLOW
      elif ultimo != None and ic + offset == ultimo:
        color = colorama.Fore.CYAN
      else:
        color = colorama.Fore.RESET

      linhas[i] += color + linha + colorama.Fore.RESET

  return '\n'.join(linhas)

def chunks(lista, n):
    resultado = []
    for i in range(0, len(lista), n):
      resultado.append(lista[i:i + n])

    return resultado

def renderiza (mesa, ultimo = None):
  size = os.get_terminal_size()
  max_cartas_por_linha = math.floor(size[0] / largura_carta)
  for i, cartas in enumerate(chunks(mesa, max_cartas_por_linha)):
    offset = i*max_cartas_por_linha
    print(linha_cartas(mesa, cartas, ultimo, offset))