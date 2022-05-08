import random

R_atb="Man nepatīk neko ēst, jo es, acīmredzot esu bots!"
R_padoms="Tavā vietā es ietu internetā un ierakstītu tieši to, ko tu tur rasktīji!"

def nezina():
    atbilde=["Vai Jūs,lūdzu,varētu pārfrāzēt jautājumu?","...",
    "Ko Jūs ar to domājat?","Izklausas labi!"][random.randrange(4)]
    return atbilde

