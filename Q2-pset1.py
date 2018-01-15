'''
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
c = 0
count = 0
for letter in s:
    if letter != 'b':
        c = c+1
    else:
        if s[c:c+3] == 'bob':
            count = count + 1
            c = c+1
        else:
            c = c+1
            continue
print(count)
