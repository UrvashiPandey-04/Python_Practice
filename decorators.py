# user defined decorator
# def mydecorator(Func):
#     def wrapper():
#         print('***')
#         Func()
#         print('***')
#     return wrapper
# @mydecorator
# def hello():
#     print('hello')
# a=mydecorator(hello)
# a()

def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0])==data_type:
                func(*args)
            else:
                raise TypeError('type mismatch')
        return inner_wrapper
    return outer_wrapper
@sanity_check(int)
def square(num):
    print(num**2)
square('a')
