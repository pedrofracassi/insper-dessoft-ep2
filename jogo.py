import baralho
import utils
import colorama

def input_validado (texto_primeiro, validacao, tuple_args):
  resultado = input(texto_primeiro)
  while not validacao(resultado, *tuple_args)[0]:
    erro, texto_erro = validacao(resultado, *tuple_args)
    resultado = input(texto_erro)

  return resultado

def valida_input_carta (resultado, min, max, mesa, monte):
  if resultado.upper() == 'M':
    if len(monte) > 0:
      return True, ''
    else:
      return False, f'Não há nenhuma carta no monte. Escolha um número entre {1} e {len(mesa)}: '

  try:
    int(resultado)
  except:
    return False, f'O valor digitado não é um número. Escolha um número entre {1} e {len(mesa)}: '

  if int(resultado) > max or int(resultado) < min:
    return False, f'Número inválido. Escolha um número entre {1} e {len(mesa)}: ',
  
  if baralho.lista_movimentos_possiveis(mesa, (int(resultado)-1))==[]:
    return False, f'A carta {resultado} não pode ser movida. Por favor, digite um número entre 1 e {len(mesa)}: '

  return True, ''

def valida_input_movimento (resultado):
  try:
    int(resultado)
  except:
    return False, 'O valor digitado não é um número. Escolha 1 ou 2: '

  if int(resultado) not in [1, 2]:
    return False, 'Número inválido. Escolha 1 ou 2: ',

  return True, ''

def iniciar (renderiza_cartas, cartas_iniciais):
    ultimo_empilhamento = None
  
    monte = baralho.cria_baralho()
    mesa = []

    i = 0
    while i < cartas_iniciais:
      mesa.append(monte[0])
      del monte[0]
      i += 1

    while baralho.possui_movimentos_possiveis(mesa, monte):
        utils.limpa_tela()
        renderiza_cartas(mesa, ultimo_empilhamento)

        if len(monte) > 0:
          print('\nCartas no monte:', len(monte))

        resultado_input = input_validado(
          f'\nEscolha uma carta e digite um número entre {1} e {len(mesa)}: ',
          valida_input_carta,
          (1, len(mesa), mesa, monte)
        )

        if resultado_input.upper() == 'M':
          mesa.append(monte[0])
          del monte[0]

        elif len(baralho.lista_movimentos_possiveis(mesa, (int(resultado_input) - 1))) > 0:

            numero = int(resultado_input)

            # Movimentos possíveis para a carta selecionada
            mov = baralho.lista_movimentos_possiveis(mesa, (numero - 1))

            # Se só houver um movimento possível, executa ele automaticamente
            if len(mov) == 1:
                destino = numero-1 - mov[0]
                novasequencia=baralho.empilha(mesa, (numero-1), destino)
                ultimo_empilhamento = destino

            # Se houver mais que um movimento possível, pergunta qual movimento o jogador quer
            elif len(mov) > 1:
                print('\nSobre qual carta você deseja empilhar? ')
                c0=mesa[numero-2]
                c1=mesa[numero-4]           
                print('1. {}'.format(c0)) 
                print('2. {}'.format(c1))

                pergunta1 = int(input_validado(
                  ' ',
                  valida_input_movimento,
                  ()
                ))

                destino = numero-1 - mov[pergunta1-1]
                novasequencia = baralho.empilha(mesa, numero-1, destino)
                ultimo_empilhamento = destino

            mesa = novasequencia

    if len(mesa) > 1 and len(monte) == 0:
        utils.limpa_tela()
        renderiza_cartas(mesa)
        print(f'\nNão há mais nenhum movimento possível. {colorama.Fore.RED}Você perdeu!{colorama.Fore.RESET}\n\nPontuação final: {52 - len(mesa)}/52')

    if len(mesa) == 1 and len(monte) == 0:
        utils.limpa_tela()
        renderiza_cartas(mesa)
        print(f'\n{colorama.Fore.LIGHTGREEN_Emesa}Parabéns, você ganhou!')

    input('\nPressione [Enter] para voltar ao menu.')