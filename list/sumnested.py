# a=[1,2,3,[4,5],6,7,[8,9],1,2,3,[4,5]]
# # i=0
# sum=0
# while i<len(a):
#     if type(a[i])==type(a):
#         j=0
#         while j<len(a[i]) :
#             sum=sum+a[i][j]
#             j+=1
#     else :
#         sum=sum+a[i]
#     i+=1
# print(sum)

a=[1,2,3,[4,5],6,7,[8,[9,19,[78]]],1,2,3,[4,5],9,3,3]
b=[]
i=0
while i<len(a):
    k=type(a[i])
    if k==int:
        b.append(a[i])
    elif k==list :
        j=0 
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    i+=1
print(b)
# l=0
# sum=0
# while l<len(b):
#     sum=sum+b[l]
#     l+=1
# print(sum)
        

