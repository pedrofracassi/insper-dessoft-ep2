import telas
import modo1
import modo2
import utils

while True:
  resposta = telas.menu()

  if resposta == '1':
    telas.regras()
    modo1.iniciar_jogo()
  elif resposta == '2':
    utils.limpa_tela()
    telas.imprime_logo()
    modo2.iniciar_jogo()
    input()
  else:
    utils.limpa_tela()
    telas.imprime_logo()
    print('Número inválido, pressione enter para continuar.')
    input()