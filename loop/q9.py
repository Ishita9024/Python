num=int(input("enter the number"))
i=0
while i<1 :
    if num%2==1 :
        print("Weird")
    elif num%2==0 and 2<=num<=5 :
        print("Not Weird")
    elif num%2==0 and 6<=num<=20 :
        print("Weird")
    else :
        print("Not weird")
    i+=1
