banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
my_file = open("file-question3.txt","w")
i=0
while i<len(banks_list):
    my_file.write(banks_list[i])
    my_file.write("\n")
    i+=1
my_file.close()


