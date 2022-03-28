# O/P ['e','b','c']
my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20,
    'g':400
    }
list=[]
for i in range(0,3):
    max=0
    for key in my_dict:
        if max<my_dict[key]:
            max=my_dict[key]
            s=key
    my_dict.pop(s)
    print(s)
        


            







