# You are given a list that contains some numbers.You have to print a
# list of next palindromes only if the number is greater than 10; otherwise, you will print that number.
#
# Input:
# [1, 6, 87, 43]
#
# Output:
# [1, 6, 88, 44]

a=int(input("Enter the size of list : "))
list=[]
for i in range(a):
    value=int(input("Enter the element : "))
    list.append(value)
l=[]

def pal(n):
    return str(n)==str(n)[::-1]

for i in range(a):
    if list[i]>10 :
        list[i]+=1
        a=list[i]
        while not pal(a):
            a+=1
        l.append(a)
    else:
        l.append(list[i])
print(l)

#
# def next_palindrome(n):
#     n = n+1
#     while not is_palindrome(n):
#         n += 1
#     return n
#
#
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
# if __name__ == "__main__":
#     size = int(input("Enter the size of your list\n"))
#     num_list = []
#     for i in range(size):
#         num_list.append(int(input("Enter the number of the list\n")))
#     print(f"You have entered {num_list}")
#
#     print(f"Output List: {[num_list[i] if num_list[i] < 10 else next_palindrome(num_list[i] ) for i in range(size)]}")
#
#
#     # new_list = []
#     # for element in num_list:
#     #     if element >10:
#     #         n = next_palindrome(element)
#     #         new_list.append(n)
# 
#     #     else:
#     #         new_list.append(element)
#     # print(f"Output List: {new_list}")


