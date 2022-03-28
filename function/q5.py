# def check_numbers(a,b):
#     if a%2==0 and b%2==0 :
#         return("both are even")
#     else :
#         return("both are not even")
# print(check_numbers(4,6))



def check_numbers_list(a,b) :
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0 :
            print("Both are Even")
        else :
            print("Both are Not even")
        i+=1
list1=[2, 6, 18, 10, 3, 75]
list2=[6, 19, 24, 12, 3, 87]
check_numbers_list(list1,list2)