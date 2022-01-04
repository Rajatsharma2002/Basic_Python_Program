import pickle
Dict={"name":"Raj Shekhar","age":20,"work":"softeware engineer"}

file = "some.pkl"
fileobj = open(file, 'wb')
pickle.dump(Dict, fileobj)
fileobj.close()

f=open("some.pkl","rb")
a=pickle.load(f)
print(a)


# # cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# # file = "mycar.pkl"
# # fileobj = open(file, 'wb')
# # pickle.dump(cars, fileobj)
# # fileobj.close()
#
# file = "mycar.pkl"
# fileobj = open(file, 'rb')
# mycar = pickle.load(fileobj)
# print(mycar)
# print(type(mycar))








