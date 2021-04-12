
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return True
        return True
    else:
        return False
        
def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    if is_leap(year) and month == 2:
        month_days[1] += 1

    return month_days[month-1]

   


year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

days = days_in_month(year,month)

print(f"There are {days} days")