item_set={}

with open(r'H:\PYTHON\LISTINGS\29.04.2022-lekcija\RDveikals-Fridges\Fridges.txt','r') as file:
    for line in file:
        line=line.split(' ')
        lst=[el for el in line if el]
        item_set[lst[2][:-1]]={'Brand':lst[1],'Price':lst[3]}
file.close

# for k,v in item_set.items():
#     print(k,v)

# print(item_set['RDB424E1AX']['Price'])