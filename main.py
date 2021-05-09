import math
import random
import defs

print('Paciência Acordeão')
print('==================')
print('Este jogo é um paciência acordeão e para ganhar o jogo, você deve empilhar todas as cartas.')
print('Existem 2 movimentos possíveis para você conseguir empilhar as cartas:')
print('')
print('1. Empilhar com a carta imediatamentre anterior')
print('2. Empilhar com a terceira carta anterior')
print('')
print('Para conseguir empilhar, existem duas condições para ser possivel (seguindo só uma dessas condições também contam):')
print('')
print('1. Ambas as cartas devem ser do mesmo valor')
print('2. Ambas as cartas devem ser do mesmo naipe')

jogando = True
comeca = input('Digite "jogar" para começar o jogo, se quiser parar digite "sair": ')
while jogando:
    if comeca == 'jogar':
        baralho = defs.random_baralho()        
        while defs.possui_movimentos_possiveis(baralho):
            for indice, carta in enumerate(baralho):
                print(f'{indice+1}. {carta}')

            numero = defs.pergunta_numero(f'Digite uma carta que deseja empilhar entre 1 e {len(baralho)}: ', len(baralho), 1) - 1
            movimentos = defs.lista_movimentos_possiveis(baralho, numero)
            if len(movimentos) == 1:
                print('teste')
                baralho = defs.empilha(baralho, numero, numero - movimentos[0])
            elif len(movimentos) == 2:
                for indice, carta in enumerate(movimentos):
                    print(f'{indice+1}. {carta}')
                indice = defs.pergunta_numero(f'é possível tirar essas cartas: {numero - movimentos[0] + 1} ou {numero - movimentos[1] + 1}, escolha qual: ', numero - movimentos[0] + 1, numero - movimentos[1] + 1)
                if indice == numero - movimentos[0] + 1:
                    baralho = defs.empilha(baralho, indice, numero - movimentos[0])
                elif indice == numero - movimentos[1] + 1:
                    baralho = defs.empilha(baralho, indice, numero - movimentos[1])
                else:
                    print('Numero invalido')
            else:
                break

    jogando = False