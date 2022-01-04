import requests
import pickle
url=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
a=url.text
list=a.split("\n")
lol=[i.split(",") for i in list if len(i)!=0]
# print(list)

file=open("iris.pkl","wb")
fileobj=pickle.dump(lol,file)
file.close()

f=open("iris.pkl","rb")
fobj=pickle.load(f)
print(fobj)


