 
mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over" 
a=mainStr.split()
print(a)
i=0
while i<len(a):
    if a[i]==subStr:
        i+=1
        continue
    print(a[i],end=" ")
    i+=1
print()
j=0
while j<len(a):
    if a[j]==subStr :
        print("on",end=" ")
    else :
        print(a[j],end=" ")
    j+=1



        
    