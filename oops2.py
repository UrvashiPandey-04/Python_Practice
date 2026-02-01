#encapsulation
# class atm:
#     def __init__(self,x,y):
#         self.pin=x
#         self.__balance=y
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,new_balance):
#         self.__balance=new_balance
#         return self.__balance
# a1=atm("123","5000")
# print(a1.get_balance())
# print(a1.set_balance("8000"))

#collection of object
# class person:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
# p1=person("riya","female")
# p2=person("siya","female")
# p3=person("ram","male")
#list of object
# l=[p1,p2,p3]
# for i in l:
#     print(i.name,i.gender)

#dictionary of object
# d={"p1":p1,"p2":p2,"p3":p3}
# for i in d:
#     print(i)
#     print(d[i].name)
#     print(d[i].gender)

#static variable
# class atm:
#     counter=1
#     def __init__(self):
#         self.cid=atm.counter
#         atm.counter+=1
#     @staticmethod
#     def get_counter():
#         return atm.counter
# a1=atm
# print(a1.get_counter())

#class relationship
#aggregation
# class customer:
#     def __init__(self,name,gender,address):
#         self.name=name
#         self.gender=gender
#         self.address=address
#     def print_address(self):
#         return (self.address.city,self.address.pin,self.address.country)
# class address:
#     def __init__(self,city,pin,country):
#         self.city=city
#         self.pin=pin
#         self.country=country
# add=address("Indore",1234,"India")
# cus=customer("riya","female",add)
# print(cus.print_address())

#Inheritance
# class user:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#     def login(self):
#         return("logging in")
# class student(user):
#     def __init__(self,roll_no):
#         self.roll_no=roll_no
#     def enroll(self):
#         return("enrolling in the course")
# u=user("riya","female")
# s=student(10)
# print(u.login())
# print(u.name)
# print(u.gender)
# print(s.enroll())
# print(s.roll_no)
# print(s.login())
# print(s.name)-will result in error

#polymorphism
#super keyword-method overridinng(run-time polymorphism)
# class phone:
#     def __init__(self,price,brand,camera):
#         print("inside phone constructor")
#         self.price=price
#         self.brand=brand
#         self.camera=camera
#     def buy(self):
#         return "buying a phone"
# class smartphone(phone):
#     def __init__(self,price,brand,camera,os,ram):
#         print("inside smartphone constructor")
#         super().__init__(price,brand,camera)
#         self.os=os
#         self.ram=ram
#         print("inside smartphone constructor")
#     def buy(self):
#         print ("buying a smartphone")

# s=smartphone(200000,"apple",60,"mac",16)
# print(s.buy())

 #method overloading- doesn't exist in python but can be implemented using
#1. default argumnets
# class test:
#     def add(self,a,b,c=0):
#         return(a+b+c)
# t=test()
# print(t.add(1,2))
# print(t.add(2,3,4))

#2. using *args
# class test:
#     def add(self,*args):
#         total=0
#         for i in args:
#             total+=i
#         return total
# t=test()
# print(t.add(5,6,7,8))
# print(t.add(8))

#3. conditional logic
# class test:
#     def add(self,a=None,b=None,c=None):
#         if(a and b and c):
#             return(a+b+c)
#         elif(a and b):
#             return(a+b)
#         else:
#             return(a)
# t=test()
# print(t.add(4,5,6))
# print(t.add(6,7))
# print(t.add(4))

#operator overloading
# print('hello'+'world')- concatenation
# print([4,5,6]+[1,2])-merging
# print(2+3)-sum

#abstraction
from abc import ABC ,abstractmethod
class bankapp(ABC):
    def database(self):
        print("connected to database")
    @abstractmethod
    def security(Self):
        pass
class mobileapp(bankapp):
    def mobile_login(self):
        print("login successful")
    def security(self):
        print("mobile security")
m=mobileapp()
print(m.security())