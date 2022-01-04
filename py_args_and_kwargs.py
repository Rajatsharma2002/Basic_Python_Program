
# def funargs(normal, *argsrohan, **kwargsbala):
#     print(normal)
#     for item in argsrohan:
#         print(item)
#     print("\nNow I would Like to introduce some of our heroes")
#     for key, value in kwargsbala.items():
#         print(f"{key} is a {value}")
#
#
# # function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")
#
# har = ["Harry", "Rohan", "Skillf", "Hammad",
#        "Shivam", "The programmer"]
# normal = "I am a normal Argument and the students are:"
# kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
#       "The Programmer": "Coordinator", "Shivam": "Cook"}
# funargs(normal, *har, **kw)


def func(n,*args,**kwargs):
    print(n)
    for i in args:
        print(i)
    for item,value in kwargs.items():
        print(f"{item} can have {value}")

n=input()
list=["Manali","Goa","Masoorie","Nanital","Moorni"]
dict={"Bike":"KTM",
      "Car":"Creata",
      "Aeroplane":"kingfisher"}

func(n,*list,**dict)