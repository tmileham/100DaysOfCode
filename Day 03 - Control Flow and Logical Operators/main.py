#########
# Day 3 Exercise
# Odd or even
#########

number = int(input("Enter your number: "))

if number % 2  == 0:
    print("Number is even")
else:
    print("Number is odd")

##########
# Day 3 - Improved BMI Calculator
##########

height = float(input("Enter your height: (in metres)"))
weight = int(input("Enter your weight: (kg)"))

bmi = round(weight / height ** 2)

print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You are a normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are overweight")
elif bmi >= 30 and bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")


########
# Day 3 - Leap Year Calculator
########

year = int(input("Please enter the year which you wish to check if its a leap year: "))

if year % 4 == 0:
    leap = True
    if year % 100 == 0:
        leap = False
        if year % 400 == 0:
            leap = True
else:
    leap = False
    
if leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#######
# Day 3 - Pizza Order
#######

totalprice = 0
size = input("What size pizza would you like? Enter S/M/L :")

if size.upper() == "L":
    totalprice += 25
elif size.upper() == "M":
    totalprice += 20
else:
    totalprice += 15

pepperoni = input("Would you like pepperoni? Y/N :")
cheese = input("Do you want extra cheese? Y/N :")

if pepperoni.upper() == "Y":
    if size == "M" or "L":
         totalprice += 3
    else:
        totalprice += 2

if cheese.upper() == "Y":
    totalprice += 1


print(f"The total price for your pizza is £{totalprice}")

########
# Day 3 - True Love Calculator
########

print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name_combined = name1.lower() + name2.lower()

true = name_combined.count("t") + name_combined.count("r") + name_combined.count("u") + name_combined.count("e")
love = name_combined.count("l") + name_combined.count("o") + name_combined.count("v") + name_combined.count("e")


lovescore = int(str(true) + str(love))

if lovescore < 10 or lovescore > 90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore > 40 and lovescore < 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}")
