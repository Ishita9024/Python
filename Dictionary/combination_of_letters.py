a={1:['a','b'],2:["c","d"]}
k=[]
n=[]
for j in a.values():
    for i in j:
        k.append(i)
for d in range(len(k)-2):
    n.append(k[d]+k[2])
    n.append(k[d]+k[3])
print(n)