import math
import random
import defs
import colorama

colorama.init()

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
while jogando:
    comeca = input('Digite "jogar" para começar o jogo, se quiser parar digite "sair": ')
    if comeca == 'jogar':
        baralho = defs.random_baralho()        
        while defs.possui_movimentos_possiveis(baralho):
            for indice, carta in enumerate(baralho):
                print(f'{indice+1}. {defs.colore_carta(carta)}')
            
            numero = defs.pergunta_numero(f'Digite uma carta que deseja empilhar entre 1 e {len(baralho)}: ', len(baralho), 1) - 1
            movimentos = defs.lista_movimentos_possiveis(baralho, numero)
            if len(movimentos) == 1:
                baralho = defs.empilha(baralho, numero, numero - movimentos[0])
            elif len(movimentos) == 2:
                for indice, step in enumerate(movimentos):
                    print(f'{indice+1}. {defs.colore_carta(baralho[numero-step])}')
                numero_empilha = defs.pergunta_numero(f'é possível tirar as cartas nas posições: {1} ou {2}, escolha qual: ', 2, 1) - 1
                baralho = defs.empilha(baralho, numero, numero - movimentos[numero_empilha])
            else:
                print('esta carta não tem movimentos')
        if len(baralho) == 1:
            print('Você ganhou!')
        else:
            print('Perdeu... :(')
    else:
        jogando = False