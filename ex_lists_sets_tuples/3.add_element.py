# 3. Se da codul de mai jos.
# Folositi metoda corecta pentru:
# - a adauga elementul "C++" la sfarsitul listei
# - printati lista

# code start
my_list = [10, 10.5, 20, 30, "Python", "Java", "Ruby"]
new_element = "C++"

# 1st method
my_list.append(new_element)
print(my_list)

# 2nd method
# my_list.extend([new_element])
# # doesnt work: my_list.extend(new_element),  result: [..., 'C', '+', '+']
# print(my_list)

# 3rd method
# my_list.insert(len(my_list), new_element)
# print(my_list)

# 4th method
# new_list = my_list + [new_element]
# print(new_list)

# code end
