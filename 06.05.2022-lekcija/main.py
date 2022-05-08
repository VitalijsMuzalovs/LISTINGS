import re
import gara_atbilde as gara

def zinjojuma_varbutiba(lieto_zinja,atpazitie_vardi,vienk_atbilde=False,prasitie_vardi=[]):
    zinojuma_noteiktiba=0
    ir_nepieciesami_vardi=True
    # uzskaita vārdus .....
    for vards in lieto_zinja:
        if vards in atpazitie_vardi:
            zinojuma_noteiktiba+=1
    # procentuāla varbutība
    procenti=float(zinojuma_noteiktiba)/float(len(atpazitie_vardi))
    # parbauda, vai virknē ir nepiecieshamie vardi
    for vards in prasitie_vardi:
        if vards not in lieto_zinja:
            ir_nepieciesami_vardi=True
            break
    if ir_nepieciesami_vardi or vienk_atbilde:
        return int(procenti*100)
    else:
        return 0

def parb_visas_atbildes(zinja):
    augst_saraksts={}

    def ATBILDE(bot_atbilde,vardu_saraksts,vienk_atbilde=False,prasitie_vardi=[]):
        vardu_saraksts = [i.lower() for i in vardu_saraksts]
        nonlocal augst_saraksts
        augst_saraksts[bot_atbilde]=zinjojuma_varbutiba(zinja,vardu_saraksts,vienk_atbilde,prasitie_vardi)
    
    # atbildes
    ATBILDE('Labdien!',['sveiki','sveiks','čau','labdien'] ,vienk_atbilde=True)
    ATBILDE('Man iet labi.Kā Tev?',['kā','tev','iet'],prasitie_vardi=['kā','tev','?'])
# .....
        # garās atbildes
    ATBILDE(gara.R_padoms,['dot','padoms'],prasitie_vardi=['padoms'])
    ATBILDE(gara.R_atb,['kas','vai','ēst'],prasitie_vardi=['tev','ēst'])

    atbilst=max(augst_saraksts,key=augst_saraksts.get)

    # for key, value in augst_saraksts.items():
    #     print(key, value)
    # print('='*30)

    return gara.nezina() if augst_saraksts[atbilst]<1 else atbilst


def panemt_zinju(lietotajs_ievada):
    sadala_zinju=re.split(r'\s+|[,;?!.-]\s*',lietotajs_ievada.lower())
    atbilde=parb_visas_atbildes(sadala_zinju)
    return atbilde

    

# testē atbildes sistēmu
while True:
    print('='*30)
    print('Bots saka:' + panemt_zinju(input('Es saku:')))
    
