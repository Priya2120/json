# Tumhare pass four employes ki details hai list mai:- ab aapko 4 
# dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4. 
# har ek employee ka dictionary main name,designation,age and salary 
# honi chahiye. aur ye sab dictionary ki keys hai jismai maine list 
# main value di hai. Iska use kar ke aapko ek json file create 
# karni hai? Jaise ki niche diya hai.


import json
list1=["neelam","programer","24","2400",]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"] 
keys=["name","designation","age","salary"]
emp1={}
emp2={}
emp3={}
emp4={}
dict1={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
for i in range(len(list1)):
    emp1.update({keys[i]:list1[i]})
for j in range(len(list2)):
    emp2.update({keys[j]:list2[j]})
for k in range(len(list3)):
    emp3.update({keys[k]:list3[k]})
for a in range(len(list4)):
    emp4.update({keys[a]:list4[a]})
with open("priya.json","w")as g:
    json.dump(dict1,g,indent=2)
    


