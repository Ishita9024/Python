num=int(input("enter:"))
a=[1,2,3,4,5,6,7,8,9,10]
k=[]
i=0
while i<len(a)-num :
    k.append(a[i])
    i+=1
j=1
while j<=num :
    k.append(a[-j])
    j+=1
print(k)