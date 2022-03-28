dic={'ishu':10,'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dic1={}
# Ascending
for i in dic:
    s=dic[i]
    for i in dic:
        a=dic[i]
        if s>a:
            dic1[i]=a
for i in dic:
    s=dic[i]
    for i in dic:
        a=dic[i]
        if s<a:
            dic1[i]=a
print(dic1)

# Descending
# for i in dic:
#     s=dic[i]
#     for i in dic:
#         a=dic[i]
#         if s<a:
#             dic1[i]=a
# for i in dic:
#     s=dic[i]
#     for i in dic:
#         a=dic[i]
#         if s>a:
#             dic1[i]=a
# print(dic1)

# count=0
# for y in dic:
#     count+=1
# #ascending order
# a={}
# i=0
# while i<count:
#     max_key = max(dic, key=dic.get)
#     value=dic.values()
#     max_value=max(value)
#     a[max_key]=max_value
#     dic.pop(max_key)
#     i+=1
# print(a)

# #descending order
# b={}
# j=0
# while j<count:
#     min_key = min(a, key=a.get)
#     values=a.values()
#     min_value=min(values)   
#     b[min_key]=min_value
#     a.pop(min_key)
#     j+=1
# print(b)