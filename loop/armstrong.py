num=int(input("enter the number"))
b=num
sum=0
while num>0 :
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if sum==b :
    print("armstrong")
else :
    print("not an armstrong number")

