#syntax error
# 1. index error
# l=[1,2,3,4]
# print(l[10])

# 2. module not found error
# import maths

# 3. key error
# d={'name':"riya"}
# d[age]

# 4. type error
# print(1+'a')

# 5. value error
# int('a')

# 6. name error
# print(a)

# 7. attribute error
# l=[1,2,3,4]
# l.upper()

# exception-try except block
# try:
#     with open('samples.txt','r') as f:
#         print(f.read())
# except:
#     print("file not found")

# find the error name
# try:
#     with open('samples.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     print(e.with_traceback)

# else block
# try:
#     f=open('sample.txt','r') 
# except FileNotFoundError:
#     print('file not found')
# else:
#     print(f.read())

#  finally block
# try:
#     f=open('samples.txt','r')
# except FileNotFoundError:
#     print('file not found')
# else:
#     print(f.read())
# finally:
#     print('done')

# raise exception
# class bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         if amount<0:
#             raise Exception('amount cannnot be negative')
#         if self.balance<amount:
#             raise Exception('low bank balance')
#         self.balance=self.balance-amount
# obj=bank(10000)
# try:
#     obj.withdraw(50000)
# except Exception as e:
#     print(e)
# else:
#     print(obj.balance)

# custom exception
class myexception(Exception):
    def __init__(self, message):
        print(message)

class bank:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount<0:
            raise myexception('amount cannot be negative')
        if self.balance<amount:
            raise myexception('low bank balance')
        self.balance=self.balance-amount
obj=bank(10000)
try:
    obj.withdraw(50000)
except Exception as e:
    print(e)
else:
    print(obj.balance)

