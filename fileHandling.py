f=open('sample.txt','w')
f.write("hello world")
f.write('\n how are you?')
f.close()

# f=open('sample.txt','w')
# f.write("hope you are doing okay!")
# f.close()

f=open('sample.txt','a')
f.write('hope you are doing okay!')
f.close()

# l=['hello\n','how are you\n','i am fine']
# f=open('sample.txt','a')
# f.writelines(l)
# f.close()

# f=open('sample.txt','r')
# s=f.read(10)
# print(s)
# f.close()

# f=open('sample.txt','r')
# print(f.readline(),end='')
# print(f.readline(),end='')
# f.close()

# reading entirely using readline
# f=open('sample.txt','r')
# while True:
#     data=f.readline()
#     if data=="":
#         break
#     else:
#         print(data,end=" ")

#using with
# with open('sample.txt','w') as f:
#     f.write('Hello World ')

# with open('sample.txt','r') as f:
#     print(f.read())

#seek and tell
# with open('sample.txt','r') as f:
#     print(f.read(10))
#     print(f.tell())
#     f.seek(0)
#     print(f.read(10))
#     print(f.tell())

# with open('sample.txt','w') as f:
#     print(f.write(10))- error as it is int type

#serialization and deserialization
import json
# l=[1,2,3,4]
# with open('demo.json','w') as f:
#     json.dump(l,f)

d={
    'name':'riya',
    'age':35,
    'gender':'female'}
with open('demo.json','w') as f:
    json.dump(d,f)

with open('demo.json','r') as f:
    d=json.load(f)
    print(d)
    print(type(d))