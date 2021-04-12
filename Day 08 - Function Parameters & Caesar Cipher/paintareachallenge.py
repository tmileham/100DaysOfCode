import math

# Specifies in square meters a can of paint can cover
coverage = 5

def calc_paint(height,width,coverage):
    area = height * width
    num_of_cans = math.ceil(area / coverage)
    print(f"You will need {num_of_cans} cans of paint")


height = float(input("Enter height in Meters :"))
width = float(input("Enter width in Meters :"))

calc_paint(height=height,width=width,coverage=coverage)