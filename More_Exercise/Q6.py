string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
i=0
a=[]
while i<len(string_list):
    k=string_list[i]
    if k not in a :
        a.append(k)
    i+=1
print(a)
