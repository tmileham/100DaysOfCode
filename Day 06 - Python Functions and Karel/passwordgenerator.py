import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwletters = random.choices(letters, k=nr_letters)
pwsymbols = random.choices(symbols, k=nr_symbols)
pwnumbers = random.choices(numbers, k=nr_numbers)

combinedpassword = pwletters + pwsymbols + pwnumbers

password = "".join(combinedpassword)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwletters = random.choices(letters, k=nr_letters)
pwsymbols = random.choices(symbols, k=nr_symbols)
pwnumbers = random.choices(numbers, k=nr_numbers)

combinedpassword = pwletters + pwsymbols + pwnumbers

print(f"Before shuffle: {combinedpassword}")

random.shuffle(combinedpassword)

password = "".join(combinedpassword)

print(password)


############################################
############################################
# Expert Mode - no built in random.choice functions
############################################
############################################

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_letters = []
pwd_symbols = []
pwd_numbers = []

for nums in range(nr_letters+1):
    randomletter = random.randint(1,len(letters)-1)
    pwd_letters.append(letters[randomletter])

for nums in range(nr_symbols+1):
    randomsymbols = random.randint(1,len(symbols)-1)
    pwd_symbols.append(symbols[randomsymbols])

for nums in range(nr_numbers+1):
    randomnumbers = random.randint(1,len(numbers)-1)
    pwd_numbers.append(numbers[randomnumbers])


combinedpwd = pwd_letters + pwd_numbers + pwd_symbols

strcombinedpwd = "".join(combinedpwd)

print(strcombinedpwd)