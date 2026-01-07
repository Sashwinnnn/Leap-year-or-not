year = int(input("Enter a year: "))
if year >= 1582:
 if (year % 4 != 0):
    print("its a commen year!")
 elif (year % 100 != 0):
    print("its a leap year!")
 elif (year % 400 != 0):
    print("its a commen year!")
 else:
    print("it's a leap year!")
else:
    print("Not within the Gregorian calendar period...")
