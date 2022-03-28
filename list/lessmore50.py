student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
length=len(student_marks)
index=0
less_than_50=0
more_than_50=0
while index<len(student_marks):
    if student_marks[index]<50 :
        less_than_50=less_than_50+1
    else:
        more_than_50=more_than_50+1
    index=index+1
print(less_than_50)
print(more_than_50)
