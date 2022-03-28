def numbers(num):
    i=0 
    sum=0
    while i<=num :
        if i%3==0 or i%5==0 :
            sum=sum+i
        i+=1
    return sum
print(numbers(10))