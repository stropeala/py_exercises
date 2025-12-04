# Tocmai ce am ajuns la masa, unde suntem 4 jucatori.
# Fiecare trebuie sa primeasca cate 5 carti dintr-un set standard de 52, valorile fiind:
# As, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
# Scrieti un program care sa:
# 1. Creeze deck-ul de carti si sa amestece cartile
# Random.shuffle() – ce e? documentam codul
# 2. Colectioneze numele fiecarui jucator intr-un dictionar
# Modelul dictionarului: key – numele jucatorului, value – lista de carti
# Numele se va introduce de la tastatura
# Maxim 4 jucatori, minim 2 jucatori se pot inregistra
# 3. In momentul in care se inregistreaza un nou jucator, automat va primi 5 carti random
# 4. La final, printam elementele dictionarului, pe rand

import random

# def deck():
#     simboluri = 'hearts', 'spades', 'diamonds', 'clubs'
#     Ace = []
#     Two = []
#     Three = []
#     Four = []
#     Five = []
#     Six = []
#     Seven = []
#     Eight = []
#     Nine = []
#     Ten = []
#     Jack = []
#     Queen = []
#     King = []
#     for i in simboluri:
#         Ace.append('As de ' + str(i))
#         As.append('As de ' + str(i))


# def deck_game():
#     symbols = ['hearts', 'spades', 'diamonds', 'clubs']
#     cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
#     deck = []
#     for i in cards:
#         for j in symbols:
#             deck.append(i + ' of ' + j)

#     deck_of_cards = {deck[i]:1 for i in range(4),
#         deck[i]:2 for i in range(4, 8)}
#     return deck_of_cards

# print(deck_game())


def deck_game():
    cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    symbols = ['hearts', 'spades', 'diamonds', 'clubs']
    deck_of_cards_values = {}
    for value, card in enumerate(cards, start = 1):
        for symbol in symbols:
            deck_of_cards_values[f'{card} of {symbol}'] = value
    deck_of_cards = list(deck_of_cards_values)
    random.shuffle(deck_of_cards)
    print(deck_of_cards)

deck_game()
