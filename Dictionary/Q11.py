# O/p [58,56,100]
my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20,
    'h':140
    }
a=[]
s=[]
for i in my_dict.values():
    a.append(i)
for x in range(3):
    b=max(a)
    a.remove(b)
    s.append(b)
print(s)




