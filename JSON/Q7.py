import json
import json
a=open("Text.txt","r")
b=a.read()
c=b.split()
print(c)
dic={}
i=0
while i<len(c):
    dic[c[i]]=c[i+1]
    i+=2
s=open("Q7.json","w")
t=json.dump(dic,s,indent=4)


