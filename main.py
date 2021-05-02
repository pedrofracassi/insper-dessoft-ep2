import telas
import modo1
import modo2
import utils
import jogo

while True:
  resposta = telas.menu()

  if resposta == '1':
    telas.regras()
    jogo.iniciar(modo1.renderiza, 52)

  elif resposta == '2':
    jogo.iniciar(modo2.renderiza, 5)

  else:
    utils.limpa_tela()
    telas.imprime_logo()
    print('Número inválido, pressione enter para continuar.')
    input()