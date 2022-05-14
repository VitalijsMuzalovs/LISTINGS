# Izveidot funkciju, kuras arguments ir saraksts ar mājaslapu adresēm. 
# Funkcija atgriež sarakstu ar
# top-level domain (.com, .net, .lv).
# https://www.iana.org/domains/root/db

def extract_tld(url):
    url = url.replace("/", "")
    url = url.split('.')[-1]
    return url

def extract_tld_3(url):
    url=url+'/'
    url=url[url.find('//')+len('//'):]
    url=url[:url.find('/')]
    url=url.split('.')[-1]
    return url

def extract_tlds(adresses):
    tlds = []
    for i in adresses:
        tlds.append(extract_tld_3(i))
    return tlds

addr = ['iana.org/content/abc.html', 'http://www.gov.au/dir/qqq', 'http://www.gov.no', 'https://ts.la/dir', 'deepmind.com']
print("Addresses: ", addr)
print("TLDs: ", extract_tlds(addr))