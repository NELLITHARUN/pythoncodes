# f = open("hello.txt", "r")
# print(f.read())



# num=5
# for i in range (1,11):
#     print (num,'x',i,'=',num*i)
f = open("hello.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("hello.txt", "r")
print(f.read())

