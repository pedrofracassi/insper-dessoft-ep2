import baralho
import utils

def input_validado (texto_primeiro, texto_erro, validacao, tuple_args):
  resultado = input(texto_primeiro)
  while not validacao(resultado, *tuple_args):
    resultado = input(texto_erro)

  return resultado

def valida_input_numero (resultado, min, max, x):
  try:
    int(resultado)
  except:
    return False

  if int(resultado) > max or int(resultado) < min:
    return False

  return True

def iniciar (renderiza_cartas):
    x = baralho.cria_baralho()

    while baralho.possui_movimentos_possiveis(x):
        utils.limpa_tela()
        renderiza_cartas(x)

        numero = int(input_validado(
          f'Escolha uma carta e digite um número entre {1} e {len(x)}: ',
          f'Número inválido. Escolha um número entre {1} e {len(x)}: ',
          valida_input_numero,
          (1, len(x), x)
        ))

        # while baralho.lista_movimentos_possiveis(x,(numero-1))==[]:
        #    print('A carta {} não pode ser movida. Por favor, digite um número entre 1 e {} :'.format(numero,len(x)))
        #    numero=int(input('Escolha uma carta e digite um número entre {} e {}: '.format(1,len(x))))
        
        if len(baralho.lista_movimentos_possiveis(x,(numero-1))) > 0:
            mov = baralho.lista_movimentos_possiveis(x,(numero-1))
            if len(mov)==1:
                novasequencia=baralho.empilha(x,(numero-1),mov[0])
            elif len(mov)>1:
                print('Sobre qual carta você deseja baralho.empilhar? ')
                c0=x[numero-1]
                c1=x[numero-3]           
                print('Qual movimento deseja executar 1 ou 2?')
                print('1. {}'.format(c0)) 
                print('2. {}'.format(c1))
                pergunta1 = int(input(' '))
                while pergunta1 not in [1,2]:
                    pergunta1 = int(input('Número inválido, digite 1 ou 2 '))
                novasequencia=baralho.empilha(x,numero-1,mov[pergunta1-1])  
        x=novasequencia

    if len(x)>1:
        utils.limpa_tela()
        renderiza_cartas(x)
        print('\nNão há mais nenhum movimento possível. Você perdeu!')

    if len(x)==1:
        utils.limpa_tela()
        renderiza_cartas(x)
        print('\nParabéns, você ganhou!')

    input('\nPressione [Enter] para continuar')