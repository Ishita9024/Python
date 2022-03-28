def leapyear(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return("it is a leap year")
            else:
                return("it is not a leap year")
        else:
            return("it's a leap year")
    else:
        return("it is not a leap year") 
num=int(input("enter"))     
print(leapyear(num))      