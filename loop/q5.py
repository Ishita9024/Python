# num=int(input("enter the number"))
# i=1
# while i<=num :
#     j=1
#     while j<=num:
#         print("1",end="")
#         j+=1
#     print()
#     k=1
#     while k<=num :
#         print("0",end="")
#         k+=1
#     print()
#     i+=2

rows=int(input("enter the rows"))
col=int(input("enter the columns"))
i=1
while i<=rows :
    j=1
    while j<=col :
        if i%2==1 :
            print("1",end="")
        else :
            print("0",end="")
        j+=1
    print()
    i+=1