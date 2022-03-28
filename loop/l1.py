# i=20
# while i<=100 :
#     if i%2==0 :
#         print(i)
#     i=i+1

num=int(input("enter"))
if num%3==0 or num%7==0 :
    print("wow")
elif num%7==0 :
    print("yum")
elif num%3==0 :
    print("yo")
else :
    print("opps")