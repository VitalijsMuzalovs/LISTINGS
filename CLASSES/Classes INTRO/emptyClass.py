class empty: pass

rec1=empty()
rec1.name = "Vital"
rec1.age=38

rec2=empty()
rec2.name="Marina"
rec2.job="Manager"

print(rec1.name, rec1.age)
print(rec2.name, rec2.job)

print(rec1.__dict__)
print(rec2.__dict__)