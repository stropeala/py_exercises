# 4. Create a text file named "test.txt". Open and write the following text in it:

# "
# 1. The quick brown fox jumps over the lazy dog.
# 2. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# 3. 123 Main Street, Cityville, USA.
# 4. Today's date is January 3, 2024.
# 5. Testing 1, 2, 3... This is a sample test line.
# "

# Add the necessary code in between print's parentheses in order to read
# the content of test.txt as a string and have the result printed out to the
# screen.

# code start
import os

filepath = "ex_c21/ex4/test.txt"
if os.path.isfile(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        print(content)
else:
    with open(filepath, "w") as f:
        string = "1. The quick brown fox jumps over the lazy dog.\n2. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n3. 123 Main Street, Cityville, USA.\n4. Today's date is January 3, 2024.\n5. Testing 1, 2, 3... This is a sample test line."
        f.write(string)
    with open(filepath, "r") as f:
        words = f.read()
        print(words)
# code end
