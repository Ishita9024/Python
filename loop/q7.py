num=int(input("enter the number"))
i=1
while i<=num :
   b=1
   while b<=num-i:
      print(" ", end="")
      b=b+1
   k=1
   while k<=i :
      print(k, end="")
      k=k+1
   p=i-1
   while p>0 :
      print(p, end="")
      p=p-1
   print()
   i+=1