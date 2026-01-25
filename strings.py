# s='hello'
# print(s)
# print(type(s))

# s="hello"
# print(s)
# print(type(s))

# s='''
# hello
# '''
# print(s)
# print(type(s))

#indexing
s="hello world"
# print(s[0])
# print(s[7])
# print(s[-3])

#slicing
# print(s[0:])
# print(s[2:6])
# print(s[:])
# print(s[::2])

#user-input string
# s=input("enter a string")
# print(s)

#mathematical opertion
# s1=' abcd '
# s2='pqrs '
# s3=s1+s2- concatenation operator
# print(s3)
# print(3*s1)

#length off string
# l=len(s1)
# print("length of string is",l)

#membership operator
# print('a' in s1)
# print('p' not in s2)

#comparison of string
# print(s1==s2)
# print(s1>s2)
# print(s1<s2)

#list methods
# print(s1.strip())
# print(s1.lstrip())
# print(s2.rstrip())

s="python is a programming language"
# print(s.find("python"))
# print(s.find("a"))
# print(s.rfind("g"))
# print(s.find("o",5,9))

# print(s.index("python"))
# print(s.index("a"))
# print(s.index("g"))
# print(s.index("z"))- will result in value error

# print(s.count("p"))
# print(s.count("p",0,5))

# print(s.replace("programming","high-level"))

# l=s.split(' ')
# for x in l:
#     print(x)

# s1='25-01-2026'
# l1=s1.split('-')
# for x in l1:
#     print(x)

# t=['a','b','c','d']
# s='-'.join(t)
# print(s)

# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print(s.startswith('python'))
# print(s.endswith('programmming'))

# print("abcd123".isalnum())
# print('1234'.isalpha())
# print('1323abcd'.isdigit())
# print('hello'.islower())
# print('hello'.isupper())
# print('Hello'.istitle())
# print("   ".isspace())

# name=input("enter your name:")
# age=int(input("enter your age:"))
# print("my name is {0} and my age is {1}".format(name,age))

#string questions
#reverse a string
# s="hello"
# print(s[::-1])
# print("".join(reversed(s)))

#remove duplicates
# s=input("enter a string:")
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# output=''.join(l)
# print(output)

#count the occurrence of a character
s=input("enter a string:")
d={}
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
for k,v in d.items():
    print("{}={}".format(k,v))~




