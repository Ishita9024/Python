a=int(input("enter the number"))
i=1
while a>0 :
    rem=a%10
    num=rem*i
    a=a//10
    print(num,end=" ")
    i=i*10


