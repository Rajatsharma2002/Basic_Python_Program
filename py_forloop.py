# list1 = [ ["Harry", 1], ["Larry", 2],
#           ["Carry", 6], ["Marie", 250]]
# dict1 = dict(list1)
#
# for item in dict1:
#     print(item)
# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)

list=["car",9,"bike",2,10,18,"truck",4,100]
print(list)
for x in list:
    if str(x).isnumeric() and x>6:
        print(x)