class cars:
    pass

normal_car=cars()
sports_car=cars()

normal_car.name="wagnar"
normal_car.price=120000

sports_car.name="Bugatti"
sports_car.price=1600000

print(normal_car,sports_car)
print(f"we have {normal_car.name} with price {normal_car.price}")
print(f"we have {sports_car.name} with price {sports_car.price}")