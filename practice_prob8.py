import random
# Harry bhai ka code
# def rohanMultiplication(number):
#     wrong = random.randint(0, 9)
#     table = [i * number for i in range(1, 11)]
#     table[wrong] = table[wrong] + random.randint(0, 10)
#     return table
#
# def isCorrect(table, number):
#     for i in range(1, 11):
#         if table[i-1] != i*number:
#             return i - 1
#
#     return None


def faulty_mul(n):
    list=[]
    wrong_index=random.randint(0,9)
    for i in range(1,11):
        if i==wrong_index:
            list.append(n*i+2)
        else:
            list.append(n * i)
    return list


def iscorrect(list,n):
    l=[]
    for i in range(1,11):
        l.append(n*i)
    if l==list:
        print("Table is not faulty")
    else:
        print("Table is faulty!\nTable creator is a fraud")

    #Ziping or combining the values of both list in one list
    a=[score for score in zip(l,list)]
    # print(a)
    # printing the index of incorect value
    for item,value in a:
        if item!=value:
            print(f"The incorrect value is at index : {a.index((item,value))}")

if __name__ == '__main__':
    n=int(input("Enter the number whose table you want to see : "))
    a=faulty_mul(n)
    print("Multiplication Table of given input is : " ,a)
    print("\nChecking the Table wheather its faulty or not : \n")
    iscorrect(a,n)


