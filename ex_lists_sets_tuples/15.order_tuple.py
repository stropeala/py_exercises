# 15. Se da codul de mai jos.
# Folositi metoda corecta pentru:
#  - a printa ultimul dintre elmentele tuple-ului, daca ar fi ordonate crescator

# code start
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")

# 1st method
sorted_tup = sorted(my_tup)
last_element = sorted_tup[len(sorted_tup) - 1]

print(last_element)  # ar trebui sa returneze Slovenia

# 2nd method
# sorted_tup = sorted(my_tup)
# last_element = sorted_tup[-1]

# print(last_element)  # ar trebui sa returneze Slovenia

# code end
