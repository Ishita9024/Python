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
j=0
allsum=0
countall=0
while j<len(elements):
    allsum=allsum+elements[j]
    countall+=1
    avgall=allsum/countall
    j+=1
print(counteven,"count_even")
print(countall,"count_total")
print(countodd,"count_odd")

print(sum,"sum_even")
print(sum1,"sum_odd")
print(allsum,"sum_total")

print(avgeve,"average_of_even")
print(avgodd,"average_of_odd")
print(avgall,"average_total")
