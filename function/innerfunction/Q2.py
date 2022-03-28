# def perfect(a) :
#     i=1
#     sum=0
#     while i<num:
#         if num%i==0 :
#             sum=sum+i
#         i+=1
#     if sum==num :
#         return "it is perfect no."
#     else :
#         return "it is not perfect no." 
# num=int(input("enter the number"))
# print(perfect(num))

i=1
while i<=1000 :
    b=1
    sum=0
    while b<i:
        if i%b==0 :
            sum=sum+b
        b+=1
    if sum==i :
        print(i,"it is perfect")
    else :
        pass
    i+=1

