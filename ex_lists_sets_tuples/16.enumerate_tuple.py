# 16. Se da codul de mai jos.
# Folositi metoda corecta pentru:
#  - a determina, si printa, de cate ori apare "Estonia" in tuple

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
if "Estonia" in my_tup:
    n = my_tup.count("Estonia")
    print(f"Estonia a aparut de {n} ori")

# code end
