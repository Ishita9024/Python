def add_numbers(a,b):
    sum=a+b
    return sum
print(add_numbers(56,4))


def add_numbers_list(a,b):
    i=0
    while i<len(a) :
        sum=a[i]+b[i]
        print(sum)
        i+=1
list1=[20,30,40]
list2=[10,20,40]
add_numbers_list(list1,list2)
    
