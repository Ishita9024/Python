num=[[1,"ishu",2,"e"],[2,"ishi",4],[3,"shivani"]]
dict={}
i = 0
while i<len(num):
    j = 1
    list1=[]
    while j<len(num[i]):
        list1.append(num[i][j])
        j+=1
    dict[num[i][0]]=list1
    i+=1
print(dict)

