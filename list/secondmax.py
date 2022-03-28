# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7,78] 
# i=0
# a=numbers[0]
# while i<len(numbers) :
#     if numbers[i]>a :
#         a=numbers[i]
#     i+=1
# numbers.remove(a)
# j=0
# b=numbers[0]
# while j<len(numbers) :
#     if numbers[j]>b :
#         b=numbers[j]
#     j+=1
# print(b)       

a=[2,3,41,4,1,6,7,0,9,20]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a[1]) 






