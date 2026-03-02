# def square(n):
#     for i in range(n):
#         yield i**2
# gen=square(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# for i in gen:
#     print(i)

# using range
# def ran(start,end):
#     for i in range(start,end):
#         yield i
# gen=ran(5,10)
# for i in gen:
#     print(i)

# tuple comprehension
gen=(i**2 for i in range(1,10))
for i in gen:
    print(i)