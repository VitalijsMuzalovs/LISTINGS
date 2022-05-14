# SECĪGA MEKLĒŠANA
"""
def meklet(saraksts,meklejamais):
    poz=0
    atrasts=False

    while poz<len(saraksts) and not atrasts:
        if saraksts[poz]==meklejamais:
            atrasts=True
        else:
            poz+=1
    return atrasts, poz

print(meklet([11,23,58,31,56,48,77,43,56,65,19,12,51],31))
"""

# ATLASES KĀRTOŠANAS ALGORITMS
"""
def kartot(saraksts):
    for vieta in range(len(saraksts)-1,0,-1):
        maxvieta=0
        for i in range(1,vieta+1):
            if saraksts[i]>saraksts[maxvieta]:
                maxvieta=i
                
            temp=saraksts[vieta]
            saraksts[vieta]=saraksts[maxvieta]
            saraksts[maxvieta]=temp
    return saraksts


saraksts=[12,4,8,32,56,221,24,86,55,37,32,1,80,54]

print(kartot(saraksts))
"""

# IEVIETOŠANAS KĀRTOŠANAS ALGORITMS - NEPABEIGTS!!!!!!!!!!!!!!!
"""
def kartot(saraksts):
   for i in range(1,len(saraksts)):

     vert= saraksts[i]
     pozicija = i

     while pozicija>0 and saraksts[pozicija-1]>vert:
         saraksts[pozicija]=saraksts[pozicija-1]
         pozicija = pozicija-1

     saraksts[pozicija]=vert

saraksts = [14,46,43,27,57,41,45,21,70]
kartot(saraksts)
print(saraksts)
"""

# SHELL SORTING
"""
def shell(dati):
     sadaljla = len(dati)//2
     while sadaljla > 0:   
      for sakt in range(sadaljla):
        gap_InsertionSort(dati, sakt, sadaljla)
      print("After increments of size",sadaljla, "The list is",saraksts)
      sadaljla = sadaljla // 2

def gap_InsertionSort(saraksts,sakt,sadal):
    for i in range(sakt+sadal,len(saraksts),sadal):
        esos_vert = saraksts[i]
        pozicija = i
        while pozicija >=sadal and saraksts[pozicija -sadal]>esos_vert:
            saraksts[pozicija ]=saraksts[pozicija -sadal]
            pozicija  = pozicija -sadal
        saraksts[pozicija ]=esos_vert

saraksts = [14,46,43,27,57,41,45,21,70]
shell(saraksts)
print(saraksts) 
"""
# O(n log n)

"""
Uzrakstiet Python programmu, lai kārtotu elementu sarakstu, 
izmantojot sapludināšanas kārtošanas algoritmu.
 Saskaņā ar Wikipedia "Apvienotā kārtošana (arī parasti tiek 
rakstīta sapludināšanas kārtošana) ir O(n log n) salīdzināšanas algoritms.
 Lielākā daļa ieviešanu nodrošina stabilu kārtošanu,
 kas nozīmē, ka ieviešana saglabā vienādu elementu ievades secību sakārtotajā. izvade."
"""

def savienot(saraksts):
    print("Sadala visu ",saraksts)
    if len(saraksts)>1:
        mid = len(saraksts)//2
        kreisa_puse = saraksts[:mid]
        laba_puse = saraksts[mid:]

        savienot(kreisa_puse)
        savienot(laba_puse)
        i=j=k=0       
        while i < len(kreisa_puse) and j < len(laba_puse):
            if kreisa_puse[i] < laba_puse[j]:
                saraksts[k]=kreisa_puse[i]
                i=i+1
            else:
                saraksts[k]=laba_puse[j]
                j=j+1
            k=k+1

        while i < len(kreisa_puse):
            saraksts[k]=kreisa_puse[i]
            i=i+1
            k=k+1

        while j < len(laba_puse):
            saraksts[k]=laba_puse[j]
            j=j+1
            k=k+1
    print("Merging ",saraksts)

saraksts = [14,46,43,27,57,41,45,21,70]
savienot(saraksts)
print(saraksts)