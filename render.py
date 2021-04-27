import baralho
import colorama

# TODO: Cores das cartas
# TODO: Posicionamento melhor dos naipes

def carta_colorida(carta):
    naipe = baralho.extrai_naipe(carta)
    if naipe == '♦' or naipe == '♥':
        return colorama.Fore.RED + carta + colorama.Fore.RESET
    if naipe == '♠' or naipe == '♣':
        return colorama.Fore.WHITE + carta + colorama.Fore.RESET

def carta_ascii (carta):
  naipe = baralho.extrai_naipe(carta)
  valor = baralho.extrai_valor(carta)

  return [
    '┌─────────┐',
    '│{}        │'.format(valor),
    '│         │',
    '│         │',
    '│    {}    │'.format(naipe),
    '│         │',
    '│         │',
    '│        {}│'.format(valor),
    '└─────────┘'
  ]

def linha_cartas (cartas):
  cartas_ascii = []

  for carta in cartas:
    cartas_ascii.append(carta_ascii(carta))

  linhas = []
  
  for carta in cartas_ascii:
    for i, linha in enumerate(carta):

      if len(linhas) < len(carta):
        linhas.append("")

      linhas[i] += linha

  return '\n'.join(linhas)

print(linha_cartas(['2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠']))