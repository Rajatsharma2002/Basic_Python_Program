class Cars:
    def __init__(self,name,price,model):
        self.name=name
        self.price=price
        self.model=model

    @classmethod
    def str_cov(cls,str):
        return cls(*str.split("/"))

    def print_detail(self):
        print(f"Car name is {self.name} \nPrice is {self.price} \nModel is {self.model}\n")

    @staticmethod
    def print_info(string):
        return f"Hello {string}"

if __name__ == '__main__':
    a=Cars.str_cov("Bugatti/400000/2018")
    b=Cars.str_cov("Audi/563673/2020")

    print(a.print_info("how are you sir"))
    a.print_detail()

    print(b.print_info("how are you sir"))
    b.print_detail()

