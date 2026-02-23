# 5. Add the necessary code on line 8 in order to bring back the cursor at the
# very beginning of test.txt before reading from the file once again.

# code start
filepath = "ex_c21/ex5/test.txt"
f = open(filepath, "r")
f.read()
f.seek(0)
print(f.read())
# code end
