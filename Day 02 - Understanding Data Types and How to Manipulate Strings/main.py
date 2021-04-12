print("Welcome to the trip calculator.")
totalcost = float(input("What was the total bill? £"))
number_of_people = int(input("How many people to split the bill?"))

tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15?"))

tip = 1 + tip_percent / 100

totalcost *= tip


bill_per_person = totalcost / number_of_people

# Using the format method to set the decimal places to 2.
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay £{final_amount}")


###############
# Day 2 Exercise

userinput = input("Enter a two digit number")

digit1 = int(userinput[0])
digit2 = int(userinput[1])

print(digit1 + digit2)

##############
# Day 2 Exercise - BMI Calculator

height = float(input("Enter your height: (in metres)"))
weight = int(input("Enter your weight: (kg)"))

bmi = round(weight / height ** 2)

print(f"Your BMI is {bmi}")




