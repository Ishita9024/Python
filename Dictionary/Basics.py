# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population)) 

# Dict = {
#        'ball' : 'green',
#        'ball': 'red'
#      }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat']) 

# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print(len(Dic)

# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# # mydict=classes.copy()
# print(classes)

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dict={"dic1":dic1,"dic2":dic2,"dic3":dic3}
# print(dict)

# dic={1:"aa",2:"bb",3:"c",4:"dd"}
# x=(1,2)
# y=(3,4)
# dic1=dict.fromkeys(x,y)
# print(dic1)

# dic={2:"bb",3:"c",4:"dd"}
# dic1=dic.setdefault(1,"ee")
# print(dic1)

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }

# del person['place']
# print(person)

# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print(len(Dic))

person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:'organisation'}

result = person['age'] 
x = person.get("gender")
print(person[4])
print(x)
print(result) 