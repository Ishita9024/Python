num=int(input("enter the number : "))
rev=""
while num>0:
    rev+=str(num%2)
    num//=2
print(rev[::-1])
