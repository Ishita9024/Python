# a=["sheetal","nikita","neha"]
# b=[]
# i=0
# while i<len(a):
# 	count=0
# 	j=0
# 	while j<len(a[i]):
# 		count+=1
# 		j+=1
# 	if count%2==0:
# 		b.append(count)
# 	i+=1
# print(b)


a=input("enter the name ")
i=0
while i<len(a):
    print(a[i],end="")
    print(" ",end="")
    i+=1
