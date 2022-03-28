name=input("enter:-")
list = []
s  = ''
for words in name:
    if words == ' ':
        list.append(s)
        s = ''
    else:
        s += words
if s :
    list.append(s)
print(list)


