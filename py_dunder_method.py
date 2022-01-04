class Employee:
    def __init__(self,name,salary,post):
        self.name=name
        self.salary=salary
        self.post=post

    def print_det(self):
        return f"name is {self.name} \nsalary is {self.salary} \npost is {self.post}"

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.post}')"

    def __str__(self):
        return f"name is {self.name} \nsalary is {self.salary} \npost is {self.post}"

    def __is_not__(self, other):
        return self.salary is not other.salary


a=Employee("Raj",555,"trainer")
b=Employee("ram",89,"cleaner")

print("overloading add : ",a+b)
print("overloading division : " ,a/b)
print("Overloading bitwise is not  : ",a is not b)

#str method will be prefreed then repr if not declared
print(a)    #output before repr method <__main__.Employee object at 0x000001E8DD948FD0>
print(repr(a))