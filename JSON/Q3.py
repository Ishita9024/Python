# Python object ko json string mai convert karne ka program likho?
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)



