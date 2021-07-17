# Python object ko json data main convert karne ka program likho? 

import json

a={    "name": "David",
    "class":"I",
    "age": 6  
}
file=open("que 1.json","w")
json.dump(a,file,indent=6)
file.close()
