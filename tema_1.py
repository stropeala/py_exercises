# String1 = "I am writing something that I will probably use later on"
# 1. Ce lungime are stringul
# 2. Cate cuvinte are stringul?
# 3. Cum stergem al doilea si al treilea cuvant?
# 4. Cum putem avea toate caracterele stringului CAPS? Dar lowercase?
import string

string1 = "I am writing something that I will probably use later on"

# EXERCITIUL 1
ex1 = string1
print(len(ex1))


# EXERCITIUL 2
ex2 = string1
print(len(ex2.split()))
# dar
ex2_2 = "I am writing something --  that -- I will probably use later on"
print(len(ex2_2.split())) # -- se pune ca si cuvant
# putem face asa
# https://stackoverflow.com/questions/19410018/how-to-count-the-number-of-words-in-a-sentence-ignoring-numbers-punctuation-an#:~:text=The%20statement%20above%20will%20go%20through%20each%20chunk%20of%20text%20and%20remove%20punctuations%20before%20verifying%20if%20the%20chunk%20is%20really%20string%20of%20alphabets.
# asta va parcurge fiecare fragment din text si va elimina semnele inainte de a verifica daca fragmentul este cu adevarat un sir de litere
print(sum(word.strip(string.punctuation).isalpha() for word in ex2_2.split()))


# EXERCITIUL 3
ex3 = string1
print(ex2[0:1],ex2[12:56])
print(ex2.replace("am writing",""))
print(ex2.replace("am writing","***CENSORED*** BIG BROTHER IS WATCHING ***CENSORED***"))


# EXERCITIUL 4
ex4 = string1.upper(), string1.lower() #or casefold()
print(ex4)