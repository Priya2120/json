# Apki pass ek shopping name ki ek dictionary hai Apki dictionary ka 
# use kar ke ek json file create karna hai. Aur apko kuch task perform 
# karne hai jaise ki 1. main dekhna chahta hu shopping list ko json file dekhna.

#  phir main user se poochu ga ki kon sa item khareedna chahte ho.

#  uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.

#  phir aapka wo number of items json file se remove karna hai.

#  Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.


# import json
# data={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }

# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file,indent=4)

a = [[1, 2, 3][4, 5, 6][7, 8, 9]]   
for list in a:
    for number in list:
        print(number, end=' ')

def flatten_list(n_list):
    result_list = []
    if not n_list: return result_list
    stack = [list(n_list)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
n_list = [1,2,[4,5],7,9,[10],4,6,[4,6,7,8,9],2]
print(flatten_list(n_list))

print ("priya")