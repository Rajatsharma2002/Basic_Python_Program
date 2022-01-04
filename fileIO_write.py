#only writing in the file
# f=open("hello.txt","w")
# a=f.write("hello how are you")
# print(a)

#appending the file(adding new text)
# f=open("hello.txt","a")
# a=f.write("hello how's your day\n")
# print(a)

#reading and writing the file
# f=open("hello.txt","r+")
# print(f.read())
# f.write("\nhello its been a long time")

#seek and tell function
# f=open("hello.txt","r")
# f.seek(10)
# print(f.tell())
# print(f.readline())
#
# print(f.tell())
# print(f.readline())
#
# f.close()

#with block
with open("hello.txt") as f:
    a=f.readlines()
    print(a)