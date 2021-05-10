import math
import random
from colorama import Fore

def cria_baralho():
    baralho = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    naipes = ['♠', '♣', '♥', '♦']
    baralho_cheio = []
    for naipe in range(4):
        for numero in range(4):
            carta = (baralho[numero] + naipes[naipe])
            baralho_cheio.append(carta)
    return baralho_cheio

def random_baralho():
    baralho = cria_baralho()
    baralho_aleatorio = []
    while len(baralho_aleatorio) < len(baralho):
        numero_lista = random.randint(0, len(baralho) - 1)
        carta_aleatoria = baralho[numero_lista]
        if carta_aleatoria not in baralho_aleatorio:
            baralho_aleatorio.append(carta_aleatoria)
    return baralho_aleatorio


def extrai_naipe(carta):
    return carta[-1]


def extrai_valor(valor):
    if valor == '10♣' or valor == '10♥' or valor == '10♦' or valor == '10♠':
        return valor[0:2]
    else:
        return valor[0]


def lista_movimentos_possiveis(baralho, indice):
    lista = []
    
    valor = extrai_valor(baralho[indice])
    valor_anterior = extrai_valor(baralho[indice-1])

    naipe = extrai_naipe(baralho[indice])
    naipe_anterior = extrai_naipe(baralho[indice-1])


    if indice == 0:
        return lista


    if indice <= 2:
        if valor == valor_anterior or naipe == naipe_anterior:
            lista += [1]
            return lista
        else:
            return lista
    if indice >= 3:
        valor_3_anterior = extrai_valor(baralho[indice-3])
        naipe_3_anterior = extrai_naipe(baralho[indice-3])

        if (valor == valor_anterior or naipe == naipe_anterior) and (valor == valor_3_anterior or naipe == naipe_3_anterior):
            lista += [1, 3]
            return lista
        if valor == valor_anterior or naipe == naipe_anterior:
            lista += [1]
        if valor == valor_3_anterior or naipe == naipe_3_anterior:
            lista += [3]
            return lista
        else:
            return lista


def empilha(baralho, origem, destino):
    carta = baralho.pop(origem)
    baralho[destino] = carta
    return baralho


def possui_movimentos_possiveis(baralho):
    i = 0
    while i < len(baralho):
        movimentos = lista_movimentos_possiveis(baralho, i)
        if len(movimentos) > 0:
            return True
        i += 1
    return False


def pergunta_numero(pergunta, maximo, minimo):
    while True:
        numero = int(input(pergunta))
        if numero <= maximo and numero >= minimo:
            return numero
        else:
            print('Este número não pode ser utilizado.')

def colore_carta(carta):
    naipe = extrai_naipe(carta)
    if naipe == '♣':
        return Fore.RED + carta + Fore.RESET
    elif naipe == '♥':
        return Fore.BLUE + carta + Fore.RESET
    elif naipe == '♦':
        return Fore.YELLOW + carta + Fore.RESET
    elif naipe == '♠':
        return Fore.GREEN + carta + Fore.RESET