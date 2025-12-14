# 18. Se da codul de mai jos.
# Folositi metoda corecta pentru:
#  - a determina, si printa, un tuple, format din toate elementele tuple-ului dat,
#  mai putin primele 4 elemente, folosind index negativ

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
# new_tup = my_tup[-6:]
# print(new_tup)

# 2nd method
new_tup = my_tup[-(len(my_tup) - 4) :]
print(new_tup)

# code end
