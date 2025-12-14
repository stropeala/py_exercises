# 6. Se da codul de mai jos.
# Folositi metoda corecta pentru:
# - a determina, si printa, minimul listei
# - a determina, si printa, maximul listei
# - a determina, si printa, suma elementelor listei

# code start
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
my_list.sort()  # or sorted_list = sorted(my_list) and then print(sorted_list)
print(my_list)
print(min(my_list))
print(max(my_list))
list_sum = sum(my_list)
print(list_sum)

# code end
