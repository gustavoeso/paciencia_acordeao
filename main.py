import math
import random
import defs

baralho = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
naipes = ['♠', '♣', '♥', '♦']
baralho_cheio = []
for naipe in range(4):
    for numero in range(13):
        carta = (baralho[numero] + naipes[naipe])
        baralho_cheio.append(carta)

random.shuffle(baralho_cheio)

for carta_embaralhada in range(52):
    print(baralho_cheio[carta_embaralhada])