# lai izveidotu jaunu vardnicu ,izvelkot  atslēgas no esošas vardnīcas

dict1 = {'vards':'Kate','vecums':25,'alga':1540,'pilseta':'Liepāja'}

aka=['vards','alga']
# jauna = {i:dict1[i] for i in aka}

jauna=dict()
for k in aka:
    jauna.update({k:dict1[k]})

print(jauna)