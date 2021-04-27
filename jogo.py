import baralho
import utils
import colorama

def input_validado (texto_primeiro, validacao, tuple_args):
  resultado = input(texto_primeiro)
  while not validacao(resultado, *tuple_args)[0]:
    erro, texto_erro = validacao(resultado, *tuple_args)
    resultado = input(texto_erro)

  return resultado

def valida_input_carta (resultado, min, max, x):
  try:
    int(resultado)
  except:
    return False, f'O valor digitado não é um número. Escolha um número entre {1} e {len(x)}: '

  if int(resultado) > max or int(resultado) < min:
    return False, f'Número inválido. Escolha um número entre {1} e {len(x)}: ',
  
  if baralho.lista_movimentos_possiveis(x, (int(resultado)-1))==[]:
    return False, f'A carta {resultado} não pode ser movida. Por favor, digite um número entre 1 e {len(x)}: '

  return True, ''

def valida_input_movimento (resultado):
  try:
    int(resultado)
  except:
    return False, 'O valor digitado não é um número. Escolha 1 ou 2: '

  if int(resultado) not in [1, 2]:
    return False, 'Número inválido. Escolha 1 ou 2: ',

  return True, ''

def iniciar (renderiza_cartas):
    ultimo_empilhamento = None

    x = baralho.cria_baralho()

    while baralho.possui_movimentos_possiveis(x):
        utils.limpa_tela()
        renderiza_cartas(x, ultimo_empilhamento)

        numero = int(input_validado(
          f'\nEscolha uma carta e digite um número entre {1} e {len(x)}: ',
          valida_input_carta,
          (1, len(x), x)
        ))

        # while baralho.lista_movimentos_possiveis(x,(numero-1))==[]:
        #    print('A carta {} não pode ser movida. Por favor, digite um número entre 1 e {} :'.format(numero,len(x)))
        #    numero=int(input('Escolha uma carta e digite um número entre {} e {}: '.format(1,len(x))))
        
        if len(baralho.lista_movimentos_possiveis(x,(numero-1))) > 0:
            mov = baralho.lista_movimentos_possiveis(x,(numero-1))

            if len(mov)==1:
                destino = numero-1 - mov[0]
                novasequencia=baralho.empilha(x, (numero-1), destino)
                ultimo_empilhamento = destino

            elif len(mov)>1:
                print('\nSobre qual carta você deseja empilhar? ')
                c0=x[numero-2]
                c1=x[numero-4]           
                print('1. {}'.format(c0)) 
                print('2. {}'.format(c1))

                pergunta1 = int(input_validado(
                  ' ',
                  valida_input_movimento,
                  ()
                ))

                destino = numero-1 - mov[pergunta1-1]
                novasequencia = baralho.empilha(x, numero-1, destino)
                ultimo_empilhamento = destino
        x=novasequencia

    if len(x)>1:
        utils.limpa_tela()
        renderiza_cartas(x)
        print(f'\nNão há mais nenhum movimento possível. {colorama.Fore.RED}Você perdeu!{colorama.Fore.RESET}\n\nPontuação final: {52 - len(x)}/52')

    if len(x)==1:
        utils.limpa_tela()
        renderiza_cartas(x)
        print(f'\n{colorama.Fore.LIGHTGREEN_EX}Parabéns, você ganhou!')

    input('\nPressione [Enter] para voltar ao menu.')