# a=20
# while a<=40 :
#     print(a)
#     a=a+2

# num=int(input("enter the number"))
# i=2
# while i<=num :
#     if num%i!=0 :
#         print(num)
#     i=i+1

num=int(input("enter the number"))
a=1
i = 2
while a<num:
    if num%i == 0:
        print(num, 'is not a prime number')
        break
    i = i + 1
else:
    print(num, 'is a prime number')
    a=a+1



