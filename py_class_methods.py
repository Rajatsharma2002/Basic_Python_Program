class Employee:
    leaves=10
    def __init__(self,aname,asalary,apost):           #constructor
        self.name=aname
        self.salary=asalary
        self.post=apost

    def print_details(self):
        print(f"Name is {self.name} \nSalary is {self.salary} \nPost is {self.post} \n")

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.leaves=new_leaves

a=Employee("Rajat",700000,"Python developer")
b=Employee("Rohan",300000,"web designer")

a.print_details()
b.print_details()

# Employee.change_leaves(50)
# print(Employee.leaves)
#
# a.change_leaves(20)
# print(a.leaves)
#
# b.change_leaves(5)
# print(b.leaves)
a.change_leaves(20)
print(b.leaves)
print(Employee.leaves)
