# 2. Fix the code below so that it doesn't generate a NameError.

# Hint:  The result should be:

# 20 200

# or

# 20
# 200

# code start

x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)

# code end
