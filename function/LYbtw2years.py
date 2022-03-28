def leapyear(a,b):
    while a<=b :
        if a%4==0:
            if a%100==0:
                if a%400==0:
                    print(a,"it is a leap year")
                else:
                    pass
            else:
                print(a,"it's a leap year")
        else:
            pass
        a+=1
num=int(input("enter"))
num1=int(input("enter"))     
leapyear(num,num1)     