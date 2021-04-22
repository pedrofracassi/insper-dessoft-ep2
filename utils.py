import os

# Função retirada da resposta de poke, no StackOverflow
# https://stackoverflow.com/a/2084628
def limpa_tela():
  os.system('cls' if os.name == 'nt' else 'clear')
