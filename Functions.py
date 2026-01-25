#function without return statement- default return value is None
# def hello():
#     print("hello sir/mam")
# hello()

# def hello(x):
#     print("hello!",x)
# hello("Urvashi")

# def hello(x):
#     return f"hello {x}"
# msg=hello("Urvashi")
# print(msg)

# def evenOdd(x):
#     if(x%2==0):
#         return "even"
#     else:
#         return "odd"
# result=evenOdd(16)
# print(result)

# function arguments
# default arguments
def printnum(a,b=10):
    print("a:",a)
    print("b",b)
printnum(5,6)
printnum(8)

# keyword arguments
def printname(fname,lname):
    print(fname, lname)
printname(fname="Urvashi",lname="Pandey")
printname(lname="Pandey",fname="Urvashi")

# positional arguments
def printinfo(name,age):
    print("hello my name is ",name)
    print("my age is ",age)
printinfo("Urvashi",20)

# variable length arguments
# *args
def multiply(*args):
    product=1
    for i in (args):
        product*=i
    return product
ans=multiply(1,2,3,4,5)
print(ans)

#kwargs
# def display(**kwargs):
#     for i,j in (kwargs.items()):
#         print(f"{i} ={j}")
# display(India="New Delhi", USA="New York", UAE="Dubai")

#nested function
# def f1():
#     print("function 1 which is the outer function")
#     def f2():
#         print("function 2 which is the inner function")
#     f2()
# f1()

#pass statement
#in function
# def info():
#     pass
# info()

#with conditional statements
# x=int(input("enter a number"))
# if(x>=7):
#     pass
# else:
#     print("number less than 7")

#with loops
# for i in range(5):
#     if(i == 3):
#         pass
#     print(i)

#local and global variable
# x=10
# def display():
#     x=5
#     print(x)
# display()
# print(x)
# x=10 is the global variable while x=5 is the local variable

#global keyword
# x=10
# def display():
#     global x
#     x+=5
#     print(x)
# display()

#function as first class citizen
#assigning function to a variable
# def greet():
#     return("hello")
# msg=greet()
# print(msg)

#passing function as an argument
# def greet(name):
#     return(f"hello {name}")
# def f1(f2,name):
#     return f2(name)
# print(f1(greet,"urvashi"))

#returning function from other function
# def f1():
#     def f2():
#         return "this is function 2"
#     return f2()
# print(f1())

#storing functions in data structure
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# d={
#     "add":add,
#     "subtract":subtract
# }
# print(d["add"](10,10))
# print(d['subtract'](10,5))

#lambda function
# n=lambda a,b: a if a>b else b
# print(n(10,20))

# ans=lambda x : "even" if x%2==0 else "odd"
# print(ans(56)) 
# print(ans(7))

# l=[lambda x=x :x**2 for x in range(1,5)]
# for i in l:
#     print(i())

#map function
# l=[1,2,3,4,5,6]
# print(list(map(lambda x: "even" if x%2==0 else "odd",l)))

#filter function
# def starts(w):
#     return w.startswith('a')
# l = ["apple", "banana", "avocado", "cherry", "apricot"]
# print(list(filter(starts,l)))

# l = ["apple", "banana", "avocado", "cherry", "apricot"]
# print(list(filter(lambda x: len(x)>5,l)))

#reduce function
# from functools import reduce
# def add(a,b):
#     return a+b
a=[1,2,3,4,5,6]
# print(reduce(add,a))
# print(reduce(lambda x,y : x*y,a))

#inner functions=nested function
# def f1():
#     def f2():
#         print("hello")
#     f2()
# f1()

#accessing variable from local space
# def f1():
#     a="hello"
#     def f2():
#         print(a)
#     f2()
# f1()

#non-local keyword
# def display():
#     a=45
#     def d2():
#         nonlocal a
#         a+=5
#         print(a)
#     d2()
# display()

#recursion
#factorial using recursion
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(5))

#fibonnaci series using factorial
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))