##############
# Weeks left of life exercise

print("I will calculate how many weeks you have left in your life based on living until 90 years old")

age = int(input("Enter your age: "))

weeksleft = round((90 - age) * 52)
daysleft = round((90 - age) * 365)
monthsleft = round((90 - age) * 12)


print(f"You have {weeksleft} weeks, {monthsleft} months, {daysleft} days left in your life.")