elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
counteven=0
countodd=0
while i<len(elements) :
    if elements[i]%2==0 :
        counteven+=1
    else :
        countodd+=1
    i+=1
print(counteven)
print(countodd)