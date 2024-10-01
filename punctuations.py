# Write a python program to remove punctuations from the given string?

str1 = "Hello! World's, How are you ?"
# expected output : Hello World How are you

lst = ['!',',','?',';',"'"]

str2 =''

for i in str1:
    if i not  in lst:

        str2 = str2 + i

print(str2)
