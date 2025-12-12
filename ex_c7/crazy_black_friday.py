# De black Friday, ne-am umplut cosul de cumparaturi cu 15 “necesitati” random, pretul fiecarui obiect variind de la 50 la 200.
# Cand ne apropiem de casa, realizam ca nu prea avem budget (max 1500) pentru toate cumparaturile.
# 1. Sa se alcatuiasca o baza de date de obiecte “care ne fac cu ochiul”.
# Team work.
# 2. Sa se genereze o colectie de obiecte random, la fiecare obiect stiindu-se pretul.
# Cum ne folosim de functii care nu sunt built-in?
# 3. Sa se calculeze costul total al cosului.
# 4. Daca valoarea cosului depaseste bugetul, sa se scoata pe rand cat un obiect pana cand cosul e sub buget.

import random

# necesitati = {
#     'nec1': random.randint(50, 200),
#     'nec2': random.randint(50, 200),
#     'nec3': random.randint(50, 200),
#     'nec4': random.randint(50, 200),
#     'nec5': random.randint(50, 200),
#     'nec6': random.randint(50, 200),
#     'nec7': random.randint(50, 200),
#     'nec8': random.randint(50, 200),
#     'nec9': random.randint(50, 200),
#     'nec10': random.randint(50, 200),
#     'nec11': random.randint(50, 200),
#     'nec12': random.randint(50, 200),
#     'nec13': random.randint(50, 200),
#     'nec14': random.randint(50, 200),
#     'nec15': random.randint(50, 200)
# }

# suma_totala = sum(list(necesitati.values()))


# def black_friday():
#     necesitati = [i + 1 for i in range(15)]
#     print(necesitati)
#     cos_cumparaturi = {necesitati[i]:random.randint(50, 200) for i in range(14)}
#     print(cos_cumparaturi)
#     total_cos = sum(list(cos_cumparaturi.values()))
#     print(total_cos)
#     for i in cos_cumparaturi:
#         if total_cos > 1500:
#             del cos_cumparaturi[i]
#         else:
#             pass
#     return cos_cumparaturi

# # print(black_friday())


# def black_friday2():
#     necesitati = [i + 1 for i in range(15)]
#     cos_cumparaturi = {necesitati[i]:random.randint(50, 200) for i in range(14)}
#     total_cos = sum(list(cos_cumparaturi.values()))
#     not_so_necessary = {}
#     for i, j in cos_cumparaturi.items():
#         if total_cos > 1500:
#             not_so_necessary[i] = j
#     for i, j in not_so_necessary.items():
#         del cos_cumparaturi[i]
#     return cos_cumparaturi

# # print(black_friday2())


# def black_friday3():
#     necesitati = [i + 1 for i in range(15)]
#     cos_cumparaturi = {necesitati[i]:random.randint(50, 200) for i in range(14)}
#     total_cos = sum(list(cos_cumparaturi.values()))
#     not_so_necessary = {}
#     for i, j in cos_cumparaturi.items():
#         if total_cos > 1500:
#             not_so_necessary[i] = j
#     for i, j in not_so_necessary.items():
#         cos_cumparaturi.pop(i)
#     return cos_cumparaturi

# # print(black_friday3())


# def black_friday4():
#     necesitati = [i + 1 for i in range(15)]
#     cos_cumparaturi = {necesitati[i]:random.randint(50, 200) for i in range(14)}
#     total_cos = sum(list(cos_cumparaturi.values()))
#     not_so_necessary = []
#     for i, j in cos_cumparaturi.items():
#         if total_cos > 1500:
#             not_so_necessary.append(i)
#     for i in not_so_necessary:
#         del cos_cumparaturi[i]
#     return cos_cumparaturi

# # print(black_friday4())


def black_friday5():
    necesitati = [i + 1 for i in range(15)]
    cos_cumparaturi = {necesitati[i]: random.randint(50, 200) for i in range(14)}
    total_cos = sum(cos_cumparaturi.values())
    while total_cos > 1500 and cos_cumparaturi:
        ne_necesitati = cos_cumparaturi.popitem()
        total_cos -= sum(ne_necesitati)
    return cos_cumparaturi


print(black_friday5())
