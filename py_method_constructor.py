class Employee:
    leaves=10
    def __init__(self,aname,asalary,apost):           #constructor
        self.name=aname
        self.salary=asalary
        self.post=apost

    def print_details(self):
        print(f"Name is {self.name} \nSalary is {self.salary} \nPost is {self.post} \n")

a=Employee("Rajat",700000,"Python developer")
b=Employee("Rohan",300000,"web designer")

a.print_details()
b.print_details()