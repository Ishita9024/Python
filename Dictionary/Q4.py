Dic= {
        1: 'NAVGURUKUL',
        2: 'IN',  
  	3:{    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
}
for i in Dic:
        if type(Dic[i])==type(Dic):
                for j in Dic[i]:
                        del Dic[i][j]
                        break
print(Dic)