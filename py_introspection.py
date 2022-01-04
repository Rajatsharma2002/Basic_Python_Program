class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def detail(self):
        return f"the employee is {self.fname} {self.lname}"

    @property         # ----------- using this we can call a method (email() ese nahi) but (email ese)---------------
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email not set ! set it using the setter"
        return f"{self.fname}.{self.lname}@google.com"

    @email.setter     # ------------ we can set a value for the method or function using this
    def email(self,str):
        sp=str.split("@")[0]
        self.fname=sp.split(".")[0]
        self.lname = sp.split(".")[1]

    @email.deleter     #----------- this helps us to delete the attribute without this we cannot delete it
    def email(self):
        self.lname=None
        self.fname = None

a=Employee("akshay","kumar")

# print(type(a))
# print(id(a))
# #print(id("hello"))
# print(dir(a))
# # print(dir("hello"))

import inspect
print(inspect.getmembers(a))
print(inspect.isclass(Employee))
print(inspect.ismodule(a))
print(inspect.isfunction(sum))