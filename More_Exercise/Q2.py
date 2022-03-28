numbers_of_students=int(input("enter the number"))
expense_of_per_student=int(input("enter the expense"))
total=numbers_of_students*expense_of_per_student
if total<=50000 :
    print("Hum budget k ander hai")
else :
    print("Hum budget k bahar hai")