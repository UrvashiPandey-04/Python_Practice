# class student:
#     college="acropolis"
#     def __init__(self,name,branch):
#         self.name=name
#         self.branch=branch
# s1=student("urvashi","aiml")
# print(s1.name)
# print(s1.branch)
# print(s1.college)

# class brand:
#     category="fashion"
#     def __init__(self,name,object):
#         self.brand_name=name
#         self.brand_object=object
# b1=brand("chanel","bag")
# print(b1.brand_name)
# print(b1.brand_object)
# print(b1.category)

#basic ATM class
# class atm:
#     def __init__(self,pin,balance):
#         self.pin=pin
#         self.balance=balance
# a1=atm(123,800000)
# print(a1.balance)
# print(a1.pin)

#ATM class
# class atm:
#     def __init__(self):
#         self.pin=" "
#         self.balance=0
#         self.menu()
        
        
#     def menu(self):
#         print("""
#             How can I help you??
#             1. Press 1 for creating pin
#             2. Press 2 for changing pin
#             3. Press 3 for checking the account balance
#             4. Press 4 to withdraw money
#             5. Press any key to exit
#              """)
#         n=int(input("Press the required key:"))
#         if(n==1):
#             self.create_pin()
#         elif(n==2):
#             self.change_pin()
#         elif(n==3):
#             self.check_balance()
#         elif(n==4):
#             self.withdraw()
#         else:
#             exit()
    

#     def create_pin(self):
#         user_input=input("enter your pin:")
#         self.pin=user_input
#         user_balance=int(input("enter your balance:"))
#         self.balance=user_balance
#         print("pin created successfully")
#         self.menu()

#     def change_pin(self):
#         user_input=input("enter your pin:")
#         if(self.pin==user_input):
#             new_pin=input("enter new pin:")
#             self.pin=new_pin
#             print("pin changed successfully")
#         else:
#             print("pin can't be changed")
#         self.menu()
#     def check_balance(self):
#         user_input=input("enter pin:")
#         if(self.pin==user_input):
#             print("your account balance is:",self.balance)
#         else:
#             print("incorrect pin")
#         self.menu()
#     def withdraw(self):
#         user_input=input("enter pin:")
#         if(user_input==self.pin):
#             amount=int(input("enter amount:"))
#             if(amount>0 and amount<=self.balance):
#                 self.balance-=amount
#                 print("withdrawal successful")
#                 print("current balance is:",self.balance)
#             else:
#                 print("account balance not sufficient")
#         else:
#             print("incorrect pin")
#         self.menu()

    
# a1=atm()

#fractional class(user defined data type)
# class fraction:
#     def __init__(self,x,y):
#         self.num=x
#         self.dec=y
#     def __str__(self):
#         return "{}/{}".format(self.num,self.dec)
#     def __add__(self,other):
#         new_num=self.num * other.dec+self.dec * other.num
#         new_dec=self.dec*other.dec
#         return "{}/{}".format(new_num,new_dec)
#     def __sub__(self,other):
#         new_num=self.num * other.dec-self.dec * other.num
#         new_dec=self.dec*other.dec
#         return "{}/{}".format(new_num,new_dec)
#     def __mul__(self,other):
#         new_num=self.num*other.num
#         new_dec=self.dec*other.dec
#         return "{}/{}".format(new_num,new_dec)
#     def __truediv__(self,other):
#         new_num=self.num*other.dec
#         new_dec=self.dec*other.num
#         return "{}/{}".format(new_num,new_dec)

# f1=fraction(3,4)
# f2=fraction(5,6)
# print(f1)
# print(f2)
# print(f1+f2)
# print(f1-f2)
# print(f1*f2)
# print(f1/f2)

#2D point and line on x,y coordinate
# class point:
#     def __init__(self,x,y):
#         self.x_cod=x
#         self.y_cod=y
#     def __str__(self):
#         return "<{},{}>".format(self.x_cod,self.y_cod)
#     def euclidean_distance(self,other):
#         return((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5
#     def distance_From_origin(self):
#         return((self.x_cod)**2+(self.y_cod)**2)**0.5
    
# class line:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def __str__(self):
#         return "{}x+{}y+{}=0".format(self.a,self.b,self.c)
#     def point_on_line(line,point):
#         if (line.a*point.x_cod +line.b*point.y_cod+line.c==0):
#             return "lies on line"
#         else:
#             return "does not lies on line"
#     def distance_bw_line_point(line,point):
#         return abs((line.a*point.x_cod +line.b*point.y_cod+line.c)/(line.a**2+line.b**2))

# p1=point(2,3)
# l1=line(1,1,2)
# print(p1)
# print(l1)

#accessing attributes and methods
class Person:
    def __init__(self,x,y):
        self.name=x
        self.country=y
    def greet(self):
        if(self.country=="India"):
            return ("namaste",self.name)
        else:
            return ("hello",self.name)
p1=Person("Urvashi","India")
print(p1.country) # - accessing attribute
print(p1.greet()) # - accessing methods


