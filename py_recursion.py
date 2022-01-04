# def factorial_itrative(n):
#     fact =1
#     for i in range(n):
#         fact=fact*(i+1)
#
#     return fact
#
# def factorial_recursive(n):
#     if(n==1):
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# num=int(input("enter a number : "))
# print("factorial using iterative approch : " , factorial_itrative(num))
# print("factorial using recursive approch : " , factorial_recursive(num))

def fibbo(n):
    if(n==1):
        return 0
    elif (n == 2):
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)

num=int(input("enter the length of series : "))
print("fibonacci series : ",fibbo(num))
# for i in range(1,num+1):
#     print("fibonacci series : ",fibbo(i))


# def fibbo(n):
#     if(n<=1):
#         return n
#     else:
#         return fibbo(n-1)+fibbo(n-2)
#
# num=int(input("enter the length : "))
# print("fibonacci sequence :")
# for i in range(num):
#     print(fibbo(i))