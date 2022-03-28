my_dict = {
        'data1':100,
        'data2': -54,
        'data3': 247
       }
sum=0
for i in my_dict.values() :
    sum=sum+i
print(sum)

# {{},{},{},{}}
num=int(input("enter"))
list=[]
for i in range(0,num+1):
    name=input("enter")
    age=int(input("enter"))
    a={"name":name,"age":age}
    list.append(a)
print(list)

