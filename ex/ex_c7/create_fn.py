# Se dau elementele urmatoare: 1, 2, 'three', 'orfu', 5
# Se cere sa creati o functie pentru urmatoarele subpuncte:
#     1. Adaugati elemtele intr-o lista si returnati lista
#     2. Aflati lungimea listei
#     3. Adaugati un element (nou) listei, introdus de la tastatura

# el = 1, 2, 'three', 'orfu', 5

# def ex1():
#     myList = list(el)
#     return myList
# ex1 = ex1()
# print(f'Asta este lista de elemente: {ex1}')

# def ex2():
#     listLen = len(el)
#     return listLen
# ex2 = ex2()
# print(f'Aste este lungimea listei: {ex2}')

# def ex3():
#     myList = list(el)
#     new_el = input('Adaugati un nou element listei:')
#     myList.append(new_el)
#     return myList
# ex3 = ex3()
# print(f'Noua lista: {ex3}')

el = 1, 2, "three", "orfu", 5


def create_list():
    myList = list(el)
    return myList


def get_list_length():
    listLen = len(el)
    return listLen


def add_element_to_list():
    myList = list(el)
    new_el = input("Adaugati un nou element listei:")
    myList.append(new_el)  # pyright: ignore
    return myList


print("Asta este lista de elemente:", create_list())
print("Aste este lungimea listei:", get_list_length())
print("Noua lista:", add_element_to_list())
