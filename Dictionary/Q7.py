dic=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
a=[]
for i in dic :
    for x in i.values():
        if x not in a :
            a.append(x)
print(a)
