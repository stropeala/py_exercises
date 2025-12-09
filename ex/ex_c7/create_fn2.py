# Se dau elementele urmatoare: 1, 2, “power”, “point”, 5
# Se cere sa creati cate o functie pentru urmatoarele subpuncte:
# 1. Ordoinati elementele intr-un dictionar si returnati dictionarul
# 2. Aflati lungimea listei
# 3. Adaugati un element listei, introdus de la tastatura

el = 1, 2, "power", "point", 5


def make_new_dict():
    myDict = {el[i]: el[i + 1] for i in range(len(el)) if i + 1 < len(el)}
    return myDict


def len_of_list():
    myList = list(el)
    return len(myList)


def add_new_el():
    myList = list(el)
    new_el = input("Adauga un nou element:")
    myList.append(new_el)  # pyright: ignore
    return myList


print("Se dau elementele urmatoare", el)
print("Dictionar ordonat:", make_new_dict())
print("Lungimea listei:", len_of_list())
print("Noua lista:", add_new_el())
