# Write a Python program to accept a string. Find and print the number of upper case alphabets and lower case alphabets.

str1 = 'Hello World'

# expected output : uppercase : 2, lowercase : 8
cnt_A = 0
cnt_a = 0
for i in str1:
    if ord(i) >= 65 and ord(i) <= 90:
        cnt_A = cnt_A + 1 
    elif ord(i) >= 97 and ord(i) <= 122:
        cnt_a +=1 
# + - * /
print('Uppercase : ',cnt_A,' Lowercase : ',cnt_a)