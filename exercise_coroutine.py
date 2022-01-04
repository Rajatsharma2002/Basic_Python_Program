def co():
    import time
    names="rajat rohan vivek sejal ravi karan sarthak yash priya "
    time.sleep(5)

    while True:
        a=(yield)
        if a in names:
            print("Name found")
        else :
            print("Name not found")

c=co()
print("search started")
next(c)
print("Next method run")
c.send(input("enter name : "))
c.close()
