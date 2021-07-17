# son data ko python object main convert karne ka program likho?.
import json

a={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
file=open("que.json","w")
json.dump(a,file,indent=6)
file.close()