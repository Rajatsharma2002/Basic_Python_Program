
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = "hello"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)

# def fact(n):
#     fact =1
#     for i in range(n):
#         fact=fact*(i+1)
#
#     yield fact
# a=fact(5)
# print(a.__next__())
#
# def fibo(n):
#     a,b=0,1
#     for i in range(n):
#         yield a
#         c=a+b
#         a,b=b,c
#
# obj=fibo(4)
# # print(obj.__next__())
# # print(obj.__next__())
# # print(obj.__next__())
# # print(obj.__next__())
#
# for i in obj:
#     print(i)


