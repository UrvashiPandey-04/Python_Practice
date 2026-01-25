#for loop- used to iterate over a sequence
# for i in range(10):
#     print(i)

# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     print(i)

# t=("a","b","c","d","e")
# for i in t:
#     print(i)

# l=["a","b","c","d","e"]
# for i in range(len(l)):
#     print(l[i])

#while loop- executes until the given condition is satisfied
# i=0
# while(i<=5):
#     print(i)
#     i+=1

#infine while loop
# while(True):
#     print("hello!")

#nested loop
# for i in range(1,5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#loop control statements
#continue- used to skip the iteration
# for i in range(10):
#     if(i==7):
#         continue
#     print(i)

#break- used to break out of the loop
# for i in range(10):
#     if(i==5):
#         break
#     print(i)

#pass- used to write the empty loops
# for i in range(10):
#     pass
# print(i)

#do-while loop - no such concept in python(is implemented using while loop)
# total=0
# while True:
#     n=int(input("enter a number:"))
#     if(n==0):
#         break
#     total+=n
# print("sum of the numbers entered",total)

#else with loop
# l=[1,5,3]
# for i in l:
#     if(i%2==0):
#         print("list contains an even number")
#         break
# else:
#     print("list does not contains an even number")

#patterns 
# n=int(input("enter number:"))
# for i in range(n):
#     print("*",end=" ")

# n=int(input("enter number:"))
# for i in range (n):
#     print("*"*n)

# n=int(input("enter number:"))
# for i in range(n):
#     print((str(i+1)+" ")*n)

# n=int(input("enter number:"))
# for i in range(n):
#     print((chr(97+i)+" ")*n)

# n=int(input("enter number:"))
# for i in range(n):
#     print((chr(65+i)+" ")*n)

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print("* "*i)

# n=int(input("enter the number:"))
# for i in range (n):
#     print("* "*(n-i))

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print(" "*(n-i),"* "*i)

# n=int(input("enter the number:"))
# for i in range(n):
#     print(" "*i,"* "*(n-i))

n=int(input("enter the number:"))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)
for j in range(n):
    print(" "*j,"* "*(n-j))
#for loop- used to iterate over a sequence
# for i in range(10):
#     print(i)

# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     print(i)

# t=("a","b","c","d","e")
# for i in t:
#     print(i)

# l=["a","b","c","d","e"]
# for i in range(len(l)):
#     print(l[i])

#while loop- executes until the given condition is satisfied
# i=0
# while(i<=5):
#     print(i)
#     i+=1

#infine while loop
# while(True):
#     print("hello!")

#nested loop
# for i in range(1,5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#loop control statements
#continue- used to skip the iteration
# for i in range(10):
#     if(i==7):
#         continue
#     print(i)

#break- used to break out of the loop
# for i in range(10):
#     if(i==5):
#         break
#     print(i)

#pass- used to write the empty loops
# for i in range(10):
#     pass
# print(i)

#do-while loop - no such concept in python(is implemented using while loop)
# total=0
# while True:
#     n=int(input("enter a number:"))
#     if(n==0):
#         break
#     total+=n
# print("sum of the numbers entered",total)

#else with loop
# l=[1,5,3]
# for i in l:
#     if(i%2==0):
#         print("list contains an even number")
#         break
# else:
#     print("list does not contains an even number")

#patterns 
# n=int(input("enter number:"))
# for i in range(n):
#     print("*",end=" ")

# n=int(input("enter number:"))
# for i in range (n):
#     print("*"*n)

# n=int(input("enter number:"))
# for i in range(n):
#     print((str(i+1)+" ")*n)

# n=int(input("enter number:"))
# for i in range(n):
#     print((chr(97+i)+" ")*n)

# n=int(input("enter number:"))
# for i in range(n):
#     print((chr(65+i)+" ")*n)

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print("* "*i)

# n=int(input("enter the number:"))
# for i in range (n):
#     print("* "*(n-i))

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print(" "*(n-i),"* "*i)

# n=int(input("enter the number:"))
# for i in range(n):
#     print(" "*i,"* "*(n-i))

n=int(input("enter the number:"))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)
for j in range(n):
    print(" "*j,"* "*(n-j))