# s={10,20,30}
# l=[10,20,30,40,50,60]
# s=set(l)
# print(s)
# print(type(s))

# s={}
# print(type(s))
# s1=set({})
# print(type(s1))

#functions of set
# s1={10,20,30,40,50}
# s1.add(60)
# print(s1)
# l=[70,80,90]
# s1.update(l)
# print(s1)
# s2=s1.copy()
# print(s2)
# print(s1.pop())
# print(s1)
# print(s1.remove(20))
# print(s1.remove(80))-will result in error
# print(s1.discard(80))
# s1.clear()
# print(s1)

#mathematical operations on set
# a={10,20,30,40,50}
# b={60,70,80,90}
# print(a.union(b))
# print(a|b)

# print(a.intersection(b))
# print(a&b)

# print(a-b)
# print(a.difference(b))

# print(a.symmetric_difference(b))
# print(a^b)

#membership operator 
# s=set("hello")
# print("h" in s)
# print("e" not in s)

#set comprehension
# s={x for x in range(0,5)}
# print(s)

#indexing and slicing - doesn't support
# s=set("hello")
# print(s[0])- will result in error
# print(s[1:3])- will result in error
