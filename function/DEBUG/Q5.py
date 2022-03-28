def distance(*num):
    i=0
    while i<len(num):
        if num[i] < 20:
            print("close")
        elif num[i] < 50:
            print("median")
        else:
            print("far")
        i+=1
distance(12,43) 