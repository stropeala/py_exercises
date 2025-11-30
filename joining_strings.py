myTuple = ('1','2','3','4','5','6','7','8','9')
print(myTuple)

a = list(myTuple)
a.append('10')
print(a)

x = ', '.join(a)
print(x)

y = list(myTuple)
# print(y)

y.append('10')
y = ', '.join(y)
# print(y)

result = ''
for char in myTuple:
    result += char
    # print(result)



myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(myList)
myTuple2 = tuple(myList)
# print(myTuple2)
mySet = set(myList)
# print(mySet)

mySet2 = {0, 6, '20', 'adam', 68.09, ('ana', 'are', 'mere')}
# print(mySet2)

salut = ' '.join(str(tuple(set(myList))))
# print(salut)