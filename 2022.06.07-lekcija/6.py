#ir fails,fiailā ir teksts , noteikt vērdu biežumu
import re,operator
celsh='2022.06.07-lekcija\mans.txt'
frek_sar={}

iF=open(celsh,'r',encoding='utf-8')
s=iF.read()
iF.close()
s=s.lower()

saraksts=re.split(r'\W',s)

for wd in saraksts:
    if wd in frek_sar:
        frek_sar[wd]=frek_sar[wd]+1
    else:
        frek_sar[wd]=1
for k,v in sorted(frek_sar.items(),key=operator.itemgetter(1),reverse=True):
    print(str(v)+'.....'+ k)