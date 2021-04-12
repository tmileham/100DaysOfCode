

def calculate(num1,num2,operation):
    """Function to calcuate numbers in the given operation method. Parameter1 int, Parameter2 int, Paramter3 str"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operator")

def app():
    end_app = False
    result = float(input("What's the first number?: "))
    while not end_app:
        
        
        print("+\n-\n*\n/")
        operation = input("Pick an operation :")
        value = float(input("What's the next number?: "))

        result = round(calculate(result,value,operation),2)
        print(f"\nThe result is: {result}")

        action = input("\nWhat would you like to do next? \n\tType 'c' to continue.\n\tType 'r' to reset\n\tType 'end' to end\n")

        if action == "r":
            app()
        elif action == "c":
            end_app = False
        elif action == "end":
            end_app = True
        else:
            print("Recieved incorrect input. Ending app")
            end_app = True

app()