# 1st Method
# 
a= {
"product": [
{"name": "lux Soap","price": 20},
{"name": "T shirt","price": 500},
{"name": "Jeans","price": 999},
{"name": "headphone","price": 2000},
{"name": "TV","price": 49999},
{"name": "5star","price": 10}
    ]
}
for i in a.values() :
    max=0
    for x in range(len(a["product"])) :
        if a["product"][x]["price"]>max :
            max=a["product"][x]["price"]
    min=0
    for x in range(len(a["product"])):
        if a["product"][x]["price"]<min:
            min=a["product"][x]["price"]
        else :
            min=a["product"][x]["price"]
print(min)
print(max)

# 2nd Method
# 
# a= {
# "product": [
# {"name": "lux Soap","price": 20},
# {"name": "T shirt","price": 500},
# {"name": "Jeans","price": 999},
# {"name": "headphone","price": 2000},
# {"name": "TV","price": 49999},
# {"name": "5star","price": 10}
#     ]
# }
# b=[]
# for i in a.values():
#     for x in range(len(a["product"])) :
#         b.append(a["product"][x]["price"])
#         c=max(b)
#         d=min(b)
# print(c)
# print(d)

#3rd Method

# a= {
# "product": [
# {"name": "lux Soap","price": 20},
# {"name": "T shirt","price": 500},
# {"name": "Jeans","price": 999},
# {"name": "headphone","price": 2000},
# {"name": "TV","price": 49999},
# {"name": "5star","price": 10}
#     ]
# }
# b=[]
# s=0
# for k in a["product"]:
#     s=s+k["price"]
# for i in a["product"]:
#     b.append(i["price"])
# j=0
# l=b[j]
# y=b[j]
# while j<len(b):
#     if l<b[j]:
#         l=b[j]
#     if y>b[j]:
#         y=b[j]
#     j+=1
# print(l)
# print(y)
# print(s)


#4th Method

# a= {
# "product": [
# {"name": "lux Soap","price": 20},
# {"name": "T shirt","price": 500},
# {"name": "Jeans","price": 999},
# {"name": "headphone","price": 2000},
# {"name": "TV","price": 49999},
# {"name": "5star","price": 10}
#     ]
# }
# b=[]
# for i in a.values():
#     for j in i:
#         for k in j.values():
#             if type(k)==int:
#                 b.append(k)
#             else:
#                 pass
# j=0
# l=b[j]
# y=b[j]
# while j<len(b):
#     if l<b[j]:
#         l=b[j]
#     if y>b[j]:
#         y=b[j]
#     j+=1
# print(l)
# print(y)


