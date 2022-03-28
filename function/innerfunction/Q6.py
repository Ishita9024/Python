def driver_speed(a):
    s=70
    b=(a-s)/5
    if a<=70 :
        print("ok")
    elif a>70 and b<12:
        print(b,"points")
    else :
        print("License suspended")
num=int(input("enter the number"))
driver_speed(num)
