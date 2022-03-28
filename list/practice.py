words=["isju","isdfghjk","ishuklwasedfghjkl"]
a=[]
max=0
for i in words:
    if len(i)>max:
        max=len(i)
for i in words:
    if max==len(i):
        a.append(i)
print(a)





