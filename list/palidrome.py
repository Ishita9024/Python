# name=['m','o','m'] 
# i=0
# while i<len(name) :
#     if name[i]==name[-i-1] :
#         print("palidrome")
#         break
#     else :
#         print("not")
#         break
#     i+=1


def birthdaycakecandles(candles):
    max_candles=max(candles)
    total=0
    for i in range(len(candles)):
        if candles[i]==max_candles:
            total+=1
    return total
a=[1,4,6,5,4,5,5,5]
print(birthdaycakecandles(a))
        

