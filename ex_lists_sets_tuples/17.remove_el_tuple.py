# 17. Se da codul de mai jos.
# Folositi metoda corecta pentru:
#  - a determina, si printa, un tuple, format din toate elementele tuple-ului dat,
#  mai putin ultimele 3 elemente

# code start
my_tup = (
    "Romania",
    "Poland",
    "Estonia",
    "Bulgaria",
    "Slovakia",
    "Slovenia",
    "Estonia",
    "Romania",
    "Hungary",
    "Slovenia",
)

# 1st method
# my_list = list(my_tup)
# del my_list[-3], my_list[-2], my_list[-1]
# new_tup = tuple(my_list)
# print(new_tup)

# 2nd method
new_new_tup = my_tup[:-3]
print(new_new_tup)

# code end
