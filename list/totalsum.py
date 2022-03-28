number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19,20,16]
a=[]
i=0
while i<len(n) :
    j=1
    while j<len(n):
        if n[i]+n[j]==number :
            a.append([n[i],n[j]])
        j+=1
    i+=1
print(a)
            