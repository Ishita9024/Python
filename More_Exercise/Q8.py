list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
k=[] 
while i<len(list1):
    a=list1[i]
    if a not in k :
        k.append(list1[i])
    i+=1
j=0
while j<len(list2):
    b=list2[j]
    if b not in k :
        k.append(list2[j])
        k.sort()
    j+=1
print(k)