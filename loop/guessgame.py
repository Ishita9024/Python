n=5
i=1
while i<=5 :
    num=int(input("enter the number"))
    if num==5 :
        print("Hurray! You won the game ")
        break
    elif 1<=num<=10 and num!=5 :
        print("wrong guess")
    else :
        print("take number less than 10")
    if 5-i==0:
        print("guess finish")
    else :
        print(5-i,"chances left")
    i=i+1

# n=7
# i=1
# while i<=10 :
#     num=int(input("enter the number"))
#     if num==7 :
#         print("wohoo! Right guess")
#         break
#     elif num>7 :
#         print("your number is greater, try again")
#     else :
#         print("your number is smaller, try again")
#     print(10-i,"chances left")
#     i=i+1
