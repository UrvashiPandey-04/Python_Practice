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

l=['hello\n','how are you\n','i am fine']
f=open('sample.txt','a')
f.writelines(l)
f.close()