num=['123','234','456b','345#']
i=0
c=[]
while i<len(num):
    try:
        b=int(num[i])
        c.append(b)
    except Exception:
        pass
    i+=1
print(c)
