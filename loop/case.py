name=input("enter the name")
i=0
while i<len(name) :
    print(name.upper()[i]+name.lower()[i]*(i),end="")
    if i!=len(name):
        print("_",end="")
        i+=1