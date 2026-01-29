# t=()
# t=(10,)
# t=10
# t=10,20,30
# t=(10,20,30)
# l=[10,20,30,40]
# t=tuple(l)
# print(t)
# print(type(t))

#accessing elements of tuple
# print(t[0])
# print(t[0:2])

#immutability of tuple
# t[4]=50- will result in error
# print(t)

#mathematical operations on tuple
# t1=(10,20,30,10,40,50)
# t2=(60,70,80,90,100)
# print(t1+t2)
# print(t1*3)

#important functions of tuple
# print(len(t1))
# print(t1.count(10))
# print(t1.index(10))
# t2=sorted(t1)
# print(t2)
# print(min(t1))
# print(max(t1))

#tuple packing and unpacking
# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)
# p,q,r,s=t
# print(p,q,r,s)

#tuple comprehension-not supported by the python
# t=(x*x for x in range(0,10))
# for i in t:
#     print(i)
# print(type(t))

#WAP to take tuple from keyboard
# n=int(input("enter number of elements in tuple:"))
# t=()
# for i in range(n):
#     a=int(input("enter value:"))
#     t=t+(a,)
# print(t)