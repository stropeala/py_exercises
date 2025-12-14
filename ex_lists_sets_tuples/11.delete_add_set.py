# 11. Se da codul de mai jos.
# Folositi metodele corecte pentru:
# - a adauga "10" setului
# - a sterge 2 din set
# - a printa setul

# code start
my_set = {1, 2, 3, 4, 6, 7, 11, 10, 29}

# 1st method
my_list = list(my_set)
popped_el = my_list.pop()
new_el = "10"
my_list.append(new_el)  # pyright: ignore
my_new_set = set(my_list)
print(type(my_new_set), my_new_set)

# 2nd method
my_set.add("10") # pyright: ignore
my_set.remove(2)
print(type(my_set), my_set)

# code end
