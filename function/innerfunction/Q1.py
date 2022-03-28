def eligible_for_vote(a) :
    if a<=18 :
        return("not eligible")
    else :
        return("eligible")
num=int(input("enter the number"))        
print(eligible_for_vote(num))
