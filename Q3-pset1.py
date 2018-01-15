'''
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
'''

l=[]
y = ''
y = y+s[0]
for i in range(0, len(s)-1):
    #print("in for"+s[i]+" "+s[i+1])
    if s[i] <= s[i+1]:
        y = y+s[i+1]
        #print("in if"+s[i])
    else:
        #print("in else"+s[i])
        #y = y+s[i]
        #print(y)
        l.append(y)
        y = ''
        y = y+s[i+1]
#print(y)
l.append(y)
print(max(l, key=len))
