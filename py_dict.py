dict={"car":"audi",
      "bike":"splender",
      "city":"mohali",
      "food":{"b":"pav bhaji",
              "l":"pizza",
              "d":"bhature"}}
print(dict)
#printing values of keys
print(dict["food"])
#printing keys and items sepratly
print(dict.keys(),"\t",dict.items())
print(dict.values())

#updating the dictionary
dict.update({"sports":"cricket"})
print(dict)

#copy the values
d=dict.copy()
print(d)

#deleting elements from dict
del dict["bike"]
print(dict)

print(dict.get("sports"))