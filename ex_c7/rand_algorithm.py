# Sa se scrie un program care parcurge o lista de numere, random, de la 1 la 200.
# Cum ne folosim de functii care nu sunt built-in?
# 1. Sa se genereze lista de numere random.
# 2. Sa se printeze doar numerele pare.
# 3. Sa se printeze doar numerele care au restul 0 cand impartim la 10
# 4. Sa se alcatuiasca o lista noua cu elementele care sunt mai mari de 20, dar mai mici decat 55.
# 5. Sa se printeze lungimea listei

import random


def make_new_list():
    myList = list(range(1, 201))
    random.shuffle(myList)
    return myList


def even_nr():
    myList = list(range(1, 201))
    random.shuffle(myList)
    evenList = []
    for i in myList:
        if i % 2 == 0:
            evenList.append(i)
    return evenList


def divTen():
    myList = list(range(1, 201))
    random.shuffle(myList)
    divByTen = []
    for i in myList:
        if i % 10 == 0:
            divByTen.append(i)
    return divByTen


def make_even_newer_list():
    myList = list(range(1, 201))
    random.shuffle(myList)
    twentyTOfiftyfive = []
    for i in myList:
        if i > 20 and i < 50:
            twentyTOfiftyfive.append(i)
    return twentyTOfiftyfive


def len_of_newer_list():
    myList = list(range(1, 201))
    random.shuffle(myList)
    twentyTOfiftyfive = []
    for i in myList:
        if i > 20 and i < 50:
            twentyTOfiftyfive.append(i)
    return len(twentyTOfiftyfive)


def single_fn():
    myList = list(range(1, 201))
    random.shuffle(myList)
    evenList = []
    divByTen = []
    twentyTOfiftyfive = []
    for i in myList:
        if i % 2 == 0:
            evenList.append(i)
        if i % 10 == 0:
            divByTen.append(i)
        if i > 20 and i < 50:
            twentyTOfiftyfive.append(i)
    print(myList)
    print(evenList)
    print(divByTen)
    print(twentyTOfiftyfive)
    return len(twentyTOfiftyfive)


print(single_fn())
