# no ievadītiem vārdiem izveidot akronimu

teikums=str(input('Ievadi tekstu: '))
teksts =teikums.split()

a=''

for i in teksts:
    a=a+str(i[0].upper())

print(a)