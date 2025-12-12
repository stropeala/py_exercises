# 4. Se da codul de mai jos.
# Folositi metoda corecta pentru:
# - a adauga elementul 546 la pozitia 3
# - printati lista

# code start

# Eu am inteles ca pozitioa 3 = index 3,
# daca pozitia 3 = elementul nr. 3,
# se schimba 3 cu 2 in linia 12 si 14
my_list = [10, 10.5, 222, 30, "Python", "Java", "Ruby"]
new_element = 546
first_half_list = my_list[:3]
# print(first_half_list)
second_half_list = my_list[3:]
# print(second_half_list)
first_half_list.append(new_element)
my_new_list = first_half_list + second_half_list
print(my_new_list)

# Intre timp mi-am adus aminte de insert() :)
# Si aici se schimba 3 cu 2 in linia 25
my_list = [10, 10.5, 222, 30, "Python", "Java", "Ruby"]
new_element = 546
my_list.insert(3, new_element)
print(my_list)

# code end
