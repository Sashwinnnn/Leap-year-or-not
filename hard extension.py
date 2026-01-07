def check(year):
    if (year % 4 != 0):
        #print("Common  year!")
        return False;
        
    elif (year % 100 != 0):
        #print("Leap year!")
        return True;
    
    elif (year % 400 != 0):
        #print("Common  year!")
        return False;

    else:
        #print("Leap year!")
        return True;


year = int(input("Enter a year: "))

if year >= 1582:
    if check(year):
         print(str(year) + " is a leap year")
    else:    
        print("this is a commen year")
        ans = input("How many number of upcoming leap years do you want to know?\n")
        count = 0
        while int(ans) != count: 
            year = year + 1
            while check(year):
                year = year +1
            count = count +1
            print(str(year) + " is the next leap year")
else:
    print("Not within the Gregorian calendar period...")
    
