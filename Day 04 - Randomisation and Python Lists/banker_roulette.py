import random

names_string = input("Give me everyone's names, seperated by a comma.,")
names = names_string.split(",")

payee = random.randint(0,(len(names)-1))

print(f"{names[payee]} is going to buy the meal today")