import re
import gara_atbilde as gara

def zinjojuma_varbutiba(lieto_zinja,atpazitie_vardi,vienk_atbilde=False,prasitie_vardi=[]):
    zinojuma_noteiktiba=0
    ir_nepieciesami_vardi=False
    # uzskaita vārdus .....
    for vards in lieto_zinja:
        if vards in atpazitie_vardi:
            zinojuma_noteiktiba+=1
    # procentuāla varbutība
    procenti=float(zinojuma_noteiktiba)/float(len(atpazitie_vardi))
    # parbauda, vai virknē ir nepiecieshamie vardi
    for vards in prasitie_vardi:
        if vards in lieto_zinja:
            ir_nepieciesami_vardi=True
            break
    if ir_nepieciesami_vardi or vienk_atbilde:
        return int(procenti*100)
    else:
        return 0
def extract_prices():
    item_set={}
    with open(r'H:\PYTHON\LISTINGS\29.04.2022-lekcija\RDveikals-Fridges\Fridges.txt','r') as file:
        for line in file:
            line=line.split(' ')
            lst=[el for el in line if el]
            print(lst)
            item_set[lst[2][:-1]]={'Alias':lst[2][:-1].lower(),'Brand':lst[1],'Price':lst[3]}
            # item_set[lst[2][:-1]]={'Brand':lst[1],'Price':lst[3]}
    file.close
    return item_set

def parb_visas_atbildes(zinja):
    augst_saraksts={}

    def ATBILDE(bot_atbilde,vardu_saraksts,vienk_atbilde=False,prasitie_vardi=[]):
        nonlocal augst_saraksts
        vardu_saraksts = [i.lower() for i in vardu_saraksts]
        prasitie_vardi = [i.lower() for i in vardu_saraksts]
        augst_saraksts[bot_atbilde]=zinjojuma_varbutiba(zinja,vardu_saraksts,vienk_atbilde,prasitie_vardi)
    
    def get_price():
        items_prices=extract_prices()
        for item in zinja:
            if item in items_prices:
                price=items_prices[item]['Price']
                item_name=item
                response = f'{item_name} maksā: {price}'
                return response

    # atbildes
    ATBILDE('Labdien!',['sveiki','sveiks','čau','labdien'] ,vienk_atbilde=True)
    ATBILDE('Man iet labi.Kā Tev?',['kā','tev','iet'],vienk_atbilde=True)
    # CENA
    ATBILDE('_item_price',['kāda','cena','cik','maksā'],prasitie_vardi=['cena'])
# .....
    # garās atbildes
    ATBILDE(gara.R_padoms,['dot','padoms'],prasitie_vardi=['padoms'])
    ATBILDE(gara.R_atb,['kas','vai','ēst'],prasitie_vardi=['ēst'])

    atbilst=max(augst_saraksts,key=augst_saraksts.get)

    # for key, value in augst_saraksts.items():
    #     print(key, value)
    # print('='*30)

    if atbilst =='_item_price':
        atbilst=get_price()
        return atbilst

    return gara.nezina() if augst_saraksts[atbilst]<1 else atbilst


def panemt_zinju(lietotajs_ievada):
    sadala_zinju=re.split(r'\s+|[,;!.-]\s*',lietotajs_ievada.lower().replace('?',' ?'))
    atbilde=parb_visas_atbildes(sadala_zinju)
    return atbilde    

# testē atbildes sistēmu
while True:
    print('='*30)
    print('Bots saka:' + panemt_zinju(input('Es saku:')))
    
