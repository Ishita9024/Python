# O/P {1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={1:50,6:60}
for key in dic1:
    if key in dic2 :
        dic2[key]=dic1[key]+dic2[key] 
    else :
        dic2[key]=dic1[key] 
dic2.update(dic3) 
print(dic2) 









