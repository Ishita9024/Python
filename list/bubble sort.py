# Descending 
a=[2,3,41,4,1,6,7,0,9,20]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a[1])



# Ascending
# a=[2,3,41,4,1,6,7,0,9,22]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#         j+=1
#     i+=1
# print(a)
