# 2021.03.04, Uzd 3:
# Izveidot funkciju, kuras arguments ir mājaslapas adrese. 
# Funkcija atgriež status code.
# https://www.shoutmeloud.com/worse-funny-domain-names-websites.html
# https://www.boredpanda.com/worst-domain-names/

import requests as req

def get_code(url):
    request = req.get(url)
    return request.status_code

def response(resp):
    try:
        resp=int(resp)
    except:
        answer="Error!"

    if 100 <= resp < 200: 
        myResp="Info code!"
    elif 200 <= resp < 299:
        myResp="Success!"
    elif 300 <= resp < 399:
        myResp="Redirect!"
    elif 400 <= resp < 499:
        myResp="Client error!"
    elif 500 <= resp < 599:
        myResp="Server error!"
    else:
        myResp="Unknown error!"
    answer=str(resp)+' - '+myResp

    return answer
    
print('HTTP Response code: ', response(get_code('http://liepajniekiem.lv/')))
print('HTTP Response code: ', response(get_code('https://www.whorepresents.com/not/what/u/a/thinking/')))
print('HTTP Response code: ', response(get_code('http://httpstat.us/500')))
