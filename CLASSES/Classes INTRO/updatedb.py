import shelve

db = shelve.open('persondb')

print(len(db))
print(list(db.keys()))
bob = db['Bob Smith']
print(bob)
print(bob.getSurname())

for key in db:
    print(key,'=>',db[key])

for obj in db:
    a = db[obj]
    a.giveRaise(0.15)
    db[obj] = a

print("\n### UPDATE ###\n")

for key in sorted(db):
    print(key,'=>',db[key])