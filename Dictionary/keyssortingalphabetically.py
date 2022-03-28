b={'a':10,'bijender':45,'deepak':60,'param':20,"i":450,'anjili':30,'roshini':50,'ishu':90,'aa':120}
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
