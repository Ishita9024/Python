b={1:"i",0:"a",9:"b",5:"c",10:"d"}
#Ascending
a=[]
dic={}
for i in b:
    a.append(i)
k=0
while k<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    k+=1
for m in range(len(a)):
    dic[a[m]]=b[a[m]]
print(dic)

#Descending
a=[]
dic={}
for i in b:
    a.append(i)
k=0
while k<len(a):
    j=0
    while j<len(a)-1:
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    k+=1
for m in range(len(a)):
    dic[a[m]]=b[a[m]]
print(dic)





