# def age_cal(a):
#     if a>=0 and a<101:
#         print(f"You entered your age i.e {a}")
#         if(a==100):
#             print("You are already 100 years old")
#         else:
#             year=0
#             while(a!=100):
#                 a=a+1
#                 year+=1
#             print(f"It will take you {year} years to turn 100 years old")
#
#     elif len(str(a))==4 and a>=1900:
#         print(f"You entered your year of birth i.e. {a}")
#         year=2021
#         age=year-a
#         if(age==0):
#             print(f"You are a new born and your age is {age}")
#         elif(age>0):
#             print(f"Your age is {age}")
#         elif(age>130):
#             print(f"You are already above 100 ")
#         else:
#             print("You are not born yet")
#
#         if(age>100):
#             print("You are already 100 years old or above")
#         else:
#             while (age != 100):
#                 age = age + 1
#                 a+= 1
#             print(f"You will turn 100 year old on year {a}")
#
# def part_age(age,year):
#     if(len(str(age))==4 and age>=1900):
#         diff=year-age
#         print(f"Your age in {year} will be {diff}")
#
#     elif(age>=0 and age<101):
#         y=2021
#         while(age!=0):
#             y-=1
#             age-=1
#         diff=year-y
#         print(f"Your age in {year} will be {diff}")
#     elif(age>130):
#         print("You are oldest man alive")
#     else:
#         print("You are not yet born ")
#
# if __name__ == '__main__':
#     age=int(input("Enter your age or year of birth :"))
#     age_cal(age)
#     print("\nIf you want to see your age in a particular year")
#     year=int(input("Enter the particular year :"))
#     part_age(age,year)

yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2021 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")

