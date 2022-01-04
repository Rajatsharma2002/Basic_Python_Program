import time
from functools import lru_cache

a=int(input("How many values you want to cache : "))
@lru_cache(maxsize=a)
def work(num):
    time.sleep(num)
    print("Called successfully ........")

if __name__ == '__main__':
    work(3)
    work(6)
    work(2)
    print("calling again....")
    work(3)
    print("successfully called again.......")

     
# @lru_cache(maxsize=32)
# def some_work(n):
#     #Some task taking n seconds
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("Now running some work")
#     some_work(3)
#     some_work(1)
#     some_work(6)
#     some_work(2)
#     print("Done... Calling again")
#     input()
#     some_work(3)
#     print("Called again")


