# class Electronicdevice:
#     calling=1
#
# class pocket_gadget(Electronicdevice):
#     calling=10
#     music=20
#     def det(self):
#         print(f"Pocket gadget has calling rating : {self.calling} \nmusic rating : {self.music} functions")
# class phone(pocket_gadget):
#     gaming=100
#     def det(self):
#         print(f"Phone has calling rating : {self.calling} \nmusic rating : {self.music} \ngaming rating : {self.gaming} functions")
#
# naman=Electronicdevice()
# david=pocket_gadget()
# ram=phone()
#
# print(naman.calling)
# ram.det()


class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

# print(darry.guitar)

# electronic device
# pocket gadget
# phone



