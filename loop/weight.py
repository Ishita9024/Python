i=1
sum=0
while i<=11 :
    weight=int(input("enter the weight"))
    sum=sum+weight
    average = sum/11
    i=i+1
print(average)
if average%5==0 :
    print("yes it is a multiple")
else :
    print("No")
    
