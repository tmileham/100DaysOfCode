# Not working, logic is broken

number = int(input("Enter a number : "))

def prime_checker(number):
    is_prime = True
    if number == 1:
        print("1 is not a prime")
    else:
        for i in range(2, number):      
            if number % i == 0:
                is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
            

prime_checker(number=number)