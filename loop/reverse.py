num=int(input("enter the number"))
rev=0
while num>0 :
    rev=rev*10+num%10
    num=num//10
print(rev)


num=int(input("enter the number"))
rev=0
while num>0 :
    rev=rev*10+num%10
    num=num//10
print(rev//10*10)

num=int(input("enter the number"))
org=num
rev=0
while num>0 :
    rev=rev*10+num%10
    num=num//10
if org==rev :
    print("palidrome number",rev)
else :
    print("Not a palidrome number",rev)