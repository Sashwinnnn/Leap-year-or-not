def check(year):
    if (year % 4 != 0):
        #print("Common  year!")
        return True;
        
    elif (year % 100 != 0):
        #print("Leap year!")
        return False;
    
    elif (year % 400 != 0):
        #print("Common  year!")
        return True;

    else:
        #print("Leap year!")
        return False;


year = int(input("Enter a year: "))

if year >= 1582:
    if check(year):
        print("this is a commen year")
        ans = input("Do you wnat to know when the enxt leap year is? \n")
        ans = ans.upper()
        if ans == "YES" or "YEP":
            year = year +1
            while check(year):
                year = year +1
                
    print(str(year) + " is the next leap year")
       
else:
    print("Not within the Gregorian calendar period...")
    
