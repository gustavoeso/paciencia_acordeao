import math
import random

def cria_baralho():
    baralho = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    naipes = ['♠', '♣', '♥', '♦']
    baralho_cheio = []
    for naipe in range(4):
        for numero in range(13):
            carta = (baralho[numero] + naipes[naipe])
            baralho_cheio.append(carta)
    return baralho_cheio

def extrai_naipe(carta):
    return carta[-1]

def extrai_valor(valor):
    if valor == '10♣' or valor == '10♥' or valor == '10♦' or valor == '10♠':
        return valor[0:2]
    else:
        return valor[0]