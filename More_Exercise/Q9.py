def is_harshad_number(a):
    org=a
    sum=0
    while a:
        rem=a%10
        sum=sum+rem
        a=a//10 
    if org%sum==0 :
        return "True"
    else :
        return "False"
num=int(input("enter the number"))
print(is_harshad_number(num))



