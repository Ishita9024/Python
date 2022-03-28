list1=[]
list2=[]
for i in range(0,2):
    name_of_student=input("enter the name")
    marks_of_student=int(input("enter the marks"))
    list1.append(name_of_student)
    list2.append(marks_of_student)
    a={}
    for j in range(len(list1)):
        a[list1[j]]=list2[j]
print(a)
