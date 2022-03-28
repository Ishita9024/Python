numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7, 110, 90, 99, 120,1,199] 
i=0
a=numbers[0]
while i<len(numbers):
    if numbers[i]>a :
        a=numbers[i]
    i+=1
k=0
b=numbers[0]
while k<len(numbers):
    if numbers[k]<b :
        b=numbers[k]
    k+=1
print(a,"max")
print(b,"min")