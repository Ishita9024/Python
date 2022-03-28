import json
shopping={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
item=input("enter item: ")
count=input("enter count: ")
# i=0
# while i<len(shopping["shopping_list"]):
if item in shopping["shopping_list"].keys():
    del shopping["shopping_list"][item]
    # break
else :
    a={item:count}
    shopping["shopping_list"].update(a)
    # break
with open('Q9.json','a') as b:
    json.dump([shopping],b,indent=4)





