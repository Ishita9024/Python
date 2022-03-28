a="mehzabeen acchi hai"
b=(a.split())
i=0
while i<len(b):
    print(b[i][0].upper(),end="")
    j=1
    while j<len(b[i]):
        print(b[i][j],end="")
        j+=1
    i+=1