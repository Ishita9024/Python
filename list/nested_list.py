list=[[1,2,3],[4,5,6],[6,5,7],[6,7,8,9],[7,8,9,1]]

i=0
while i<len(list):
    j=0
    s=0
    c=0
    while j<i-1:
        s=s+list[i][j]
        c+=1
        j+=1
    i+=1
print(c)

        