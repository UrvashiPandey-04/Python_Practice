# d={}
# print(d)
# print(type(d))

# d={"a":1,"b":2,"c":3}
# print(d)
# print(type(d))
# d["a"]=3
# print(d)

#accessing data from dictionary
# print(d['a'])
# print(d['c'])
# print(d["d"])-will result in error

#dictionary entered by user at run time
# d={}
# n=int(input("enter number of elements in a dictionary:"))
# for i in range(n):
#     k=input("enter keys:")
#     v=input("enter values:")
#     d[k]=v
# print(d)

#deleting elements from dictionary
# d={"a":1,"b":2,"c":3}
# print(d)
# del d["a"]
# print(d)

# d.clear()
# print(d)

# del d
# print(d)

#important dict functions
# d=dict({"a":1,"b":2,"c":3})
# print(d)
# print(len(d))
# print(d.get("a"))
# print(d.pop("b"))
# print(d.popitem())
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# d1=d.copy()
# print(d1)
# print(d.setdefault("b",2))
# print(d)
# print(d1.update(d))
# print(d1)

#WAP to take dictionary from keyboards and print the sum values
# d={}
# sum=0
# n=int(input("enter number of elements in the dictionay:"))
# for i in range(n):
#     k=input("enter keys:")
#     v=input("enter values:")
#     d[k]=v
#     sum+=int(v)
# print(d)
# print(sum)

#WAP to find number of occurrences of each letter present in the given string
# word=input("enter a word:")
# d={}
# for i in word:
#     d[i]=d.get(i,0)+1
# for k,v in d.items():
#     print(k,"occurred",v,"times")

#dictionary comprehension
d={x:x*x for x in range(1,5)}
print(d)