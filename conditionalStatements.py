#if statement
# age=int(input("enter your age:"))
# if age>=18:
#     print("eligible to vote")

# name=input("enter your name:")
# if(name=="Urvashi"):
#     print("welcome",name)

#shorthand if statement
# age=int(input("enter your age"))
# if age>=18: print("eligible to vote")

#if-else statement
# age=int(input("enter your age:"))
# if (age>=18):
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# name=input("enter your name:")
# if(name=="Urvashi"):
#     print("hello",name)
# else:
#     print("welcome",name)

#shorthand if-else(ternary operator)
# marks=int(input("enter your marks:"))
# print("pass" if marks>=33 else "fail")

#if-elif-else statement
# marks=int(input("enter your marks:"))
# if(marks>=90):
#     print("grade A")
# elif(marks>=80):
#     print("grade B")
# elif(marks>=70):
#     print("grade c")
# elif(marks>=40):
#     print("grade D")
# else:
#     print("fail")

#nested if-else statement
# age=int(input("enter your age:"))
# is_member=True
# if(age>60):
#     if(is_member):
#         print("60% discount")
#     else:
#         print("30% discount" )
# else:
#     print("not eligible for discount")

#match case
# number=int(input("enter number:"))
# match number:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3 | 4:
#         print("three or four")
#     case _ :
#         print("other number")

#problems
#even-odd
# num=int(input("enter number:"))
# if(num%2==0):
#     print("even number")
# else:
#     print("odd number")

#greatest of three numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>=b and b>=c):
    print(a,"is the greatest")
elif(b>=c):
    print(b,"is the greatest")
else:
    print(c,"is the greatest")
