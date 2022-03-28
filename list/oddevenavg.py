elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
sum=0
sum1=0
counteven=0
countodd=0
while i<len(elements):
    if elements[i]%2==0 :
        sum=sum+elements[i]
        counteven+=1
        avgeve=sum/counteven
    else :
        sum1=sum1+elements[i]
        countodd+=1
        avgodd=sum1/countodd
    i+=1
print(avgeve,"even")
print(avgodd,"odd")
