# a="MISSISSIPPI"
# dic={}
# for i in range(len(a)):
#     count=0
#     for j in range(len(a)):
#         if a[i]==a[j]:
#             count+=1
#         dic[a[i]]=count
# print(dic)


num=[1,2,3,2,4]
dic={}
for i in num:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)

        



    



