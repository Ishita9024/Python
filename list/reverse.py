# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=0
# while i<len(places):
#     print(places[-i-1])
#     i=i+1
    
    
# a=[12350,67890,7890,57890]
# b=[]
# for i in a:
#     if i%10==0:
#         b.append(i//10)
# print(b)

# a=[4,4,5,23,23,23,23,23]
# d=max(a)
# print(a.count(d))
# max=0
# count=0
# for i in a:
#     if i>max:
#         max=i
# print(a.count(max))


a=[19,10,12,10,22,24,25]
d=[]
b=[]
k=4
sum=0
for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            pass
        else:
            sum=a[i]+a[j]
            if sum%k==0:
                pass
            else:
                b.append(a[i])
                b.append(a[j])
print(set(b))
sum1=0
for n in range(len(b)):
    for l in range(len(b)):
        if n==l:
            pass
        else:
            sum1=b[n]+b[l]
            if sum1%k==0:
                pass
            else:
                d.append(b[n])
                d.append(b[l])
print(set(d))                                
# print(set(b))
# print(len(set(b)))